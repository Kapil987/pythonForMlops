import boto3
import streamlit as st
import os
import uuid
from langchain_community.embeddings import BedrockEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

## AWS Setup
REGION = "us-east-1"
s3_client = boto3.client("s3", region_name=REGION)
bedrock_client = boto3.client(service_name="bedrock-runtime", region_name=REGION)

BUCKET_NAME = os.getenv("BUCKET_NAME")

## Initialize Embeddings
bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0", 
    client=bedrock_client
)

def get_unique_id():
    return str(uuid.uuid4())

## Split the pages / text into chunks
def split_text(pages, chunk_size, chunk_overlap):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
    )
    docs = text_splitter.split_documents(pages)
    return docs

## create vector store
def create_vector_store(request_id, documents):
    vectorstore_faiss = FAISS.from_documents(documents, bedrock_embeddings)
    file_name = f"{request_id}.bin"
    folder_path = "/tmp" # Use standard /tmp
    
    # Save local
    vectorstore_faiss.save_local(index_name=file_name, folder_path=folder_path)

    # Upload both FAISS components to S3
    # Note: save_local creates .faiss and .pkl files
    s3_client.upload_file(
        Filename=f"{folder_path}/{file_name}.faiss", 
        Bucket=BUCKET_NAME, 
        Key="my_faiss.faiss"
    )
    s3_client.upload_file(
        Filename=f"{folder_path}/{file_name}.pkl", 
        Bucket=BUCKET_NAME, 
        Key="my_faiss.pkl"
    )
    return True

def main():
    st.set_page_config("Admin - PDF Processor")
    st.write("### Admin Site: PDF to Vector Store")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        request_id = get_unique_id()
        st.info(f"Processing Request: {request_id}")
        
        saved_file_name = f"{request_id}.pdf"
        with open(saved_file_name, mode="wb") as w:
            w.write(uploaded_file.getvalue())

        # Load and Split
        loader = PyPDFLoader(saved_file_name)
        pages = loader.load_and_split()
        st.write(f"Total Pages: {len(pages)}")

        splitted_docs = split_text(pages, 1000, 200)
        st.write(f"Created {len(splitted_docs)} text chunks.")

        with st.spinner("Creating Vector Store and uploading to S3..."):
            result = create_vector_store(request_id, splitted_docs)
            if result:
                st.success("Hurray!! PDF processed and Index saved to S3.")
            else:
                st.error("Error processing the vector store.")

if __name__ == "__main__":
    main()