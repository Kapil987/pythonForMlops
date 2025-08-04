import boto3
import streamlit as st
import os
import uuid

# S3 client and configuration
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Bedrock imports
from langchain_community.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock

# Prompt and Retrieval chain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# PDF Loader and Text Splitter (if needed in your workflow)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Import FAISS for vectorstore management
from langchain_community.vectorstores import FAISS

# Initialize Bedrock client and embeddings
bedrock_client = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0", client=bedrock_client
)

folder_path = "/tmp/"

def get_unique_id():
    return str(uuid.uuid4())

## S3 missing pickle file error handling
def load_index():
    try:
        s3_client.download_file(
            Bucket=BUCKET_NAME, 
            Key="my_faiss.faiss", 
            Filename=f"{folder_path}my_faiss.faiss"
        )
        s3_client.download_file(
            Bucket=BUCKET_NAME, 
            Key="my_faiss.pkl", 
            Filename=f"{folder_path}my_faiss.pkl"
        )
    except s3_client.exceptions.ClientError as e:
        error_code = e.response["Error"]["Code"]
        if error_code == "404":
            st.error("Index files not found in S3. Please verify the files exist or generate/upload them.")
        else:
            st.error("Error downloading index files: " + str(e))
        raise e

def get_llm():
    # Initialize the Bedrock LLM with specific model kwargs
    llm = Bedrock(
        model_id="amazon.titan-text-premier-v1:0", 
        client=bedrock_client,
        model_kwargs={"maxTokenCount": 512}
    )
    return llm

def get_response(llm, vectorstore, question):
    # Define the prompt template
    prompt_template = """
    Human: Please use the given context to provide a concise answer to the question.
    If you don't know the answer, just say that you don't know; don't try to make up an answer.
    <context>
    {context}
    </context>
    Question: {question}
    Assistant:"""
    
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    
    # Create the RetrievalQA chain using the vectorstore's retriever
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_type="similarity", search_kwargs={"k": 5}
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    answer = qa({"query": question})
    return answer["result"]

def main():
    st.header("Client Site for Chat with PDF Demo using Bedrock, RAG, etc.")

    # Load index files from S3 with error handling
    try:
        load_index()
    except Exception as e:
        st.stop()  # Stop execution if index files are missing or error out
    
    # List files in folder_path to confirm files were downloaded
    dir_list = os.listdir(folder_path)
    st.write(f"Files and Directories in {folder_path}:", dir_list)
    
    # Load the FAISS index
    try:
        faiss_index = FAISS.load_local(
            index_name="my_faiss",
            folder_path=folder_path,
            embeddings=bedrock_embeddings,
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        st.error("Failed to load FAISS index. Error: " + str(e))
        st.stop()
    
    st.write("INDEX IS READY")
    
    # Get user question and process response
    question = st.text_input("Please ask your question")
    if st.button("Ask Question") and question.strip():
        with st.spinner("Querying..."):
            llm = get_llm()
            result = get_response(llm, faiss_index, question)
            st.write(result)
            st.success("Done")

if __name__ == "__main__":
    main()
