import boto3
import os
import sys
import argparse
import uuid
from langchain_aws import BedrockEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

## AWS Setup
REGION = "us-east-1"
s3_client = boto3.client("s3", region_name=REGION)
bedrock_client = boto3.client(service_name="bedrock-runtime", region_name=REGION)

BUCKET_NAME = os.getenv("BUCKET_NAME")
FOLDER_PATH = "/tmp"

if not BUCKET_NAME:
    print("Error: Environment variable BUCKET_NAME is not set.")
    sys.exit(1)

## Initialize Embeddings
bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0", 
    client=bedrock_client
)

def split_text(pages, chunk_size, chunk_overlap):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
    )
    docs = text_splitter.split_documents(pages)
    return docs

def create_vector_store(documents):
    print("Generating embeddings and vector store...")
    vectorstore_faiss = FAISS.from_documents(documents, bedrock_embeddings)
    
    # Use a temporary local name before upload
    file_name = "temp_index"
    
    # Save local to /tmp
    vectorstore_faiss.save_local(index_name=file_name, folder_path=FOLDER_PATH)

    # Upload to S3 as 'my_faiss' to match the user app expectation
    print(f"Uploading index to S3 bucket: {BUCKET_NAME}...")
    try:
        s3_client.upload_file(
            Filename=f"{FOLDER_PATH}/{file_name}.faiss", 
            Bucket=BUCKET_NAME, 
            Key="my_faiss.faiss"
        )
        s3_client.upload_file(
            Filename=f"{FOLDER_PATH}/{file_name}.pkl", 
            Bucket=BUCKET_NAME, 
            Key="my_faiss.pkl"
        )
        return True
    except Exception as e:
        print(f"Error uploading to S3: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Admin CLI: Ingest PDF to Vector Store")
    parser.add_argument("file", help="Path to the PDF file to ingest")
    args = parser.parse_args()

    file_path = args.file

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    print(f"Processing file: {file_path}")
    
    # Load and Split
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        print(f"Total Pages: {len(pages)}")

        splitted_docs = split_text(pages, 1000, 200)
        print(f"Created {len(splitted_docs)} text chunks.")

        # Create Vector Store
        if create_vector_store(splitted_docs):
            print("Success! PDF processed and Index saved to S3.")
        else:
            print("Failed to process vector store.")
            
    except Exception as e:
        print(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    main()