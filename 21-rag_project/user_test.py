import boto3
import os
import sys
# from operator import itemgetter

# Updated Imports
from langchain_aws import BedrockEmbeddings
from langchain_aws import ChatBedrock 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough 
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

def load_index_from_s3():
    print(f"Downloading index from S3 bucket: {BUCKET_NAME}...")
    try:
        s3_client.download_file(Bucket=BUCKET_NAME, Key="my_faiss.faiss", Filename=f"{FOLDER_PATH}/my_faiss.faiss")
        s3_client.download_file(Bucket=BUCKET_NAME, Key="my_faiss.pkl", Filename=f"{FOLDER_PATH}/my_faiss.pkl")
        print("Index synced successfully.")
        return True
    except Exception as e:
        print(f"Failed to find index in S3. Error: {e}")
        return False

def get_llm():
    # Note: Removed 'us.' prefix if not using cross-region inference to avoid permissions issues
    return ChatBedrock(
        model_id="amazon.nova-micro-v1:0", 
        client=bedrock_client,
        model_kwargs={'max_tokens': 512}
    )

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_response(llm, vectorstore, question):
    ## Normal prompt
    # template = """
    # Use the following pieces of context to provide a concise answer to the question at the end.
    # <context>
    # {context}
    # </context>
    # Question: {question}
    # """

    ## Chain of Thought" prompt that encourages the model to look harder
    template = """
    Human: You are a helpful banking assistant.
    Use the context below to answer the user's question. 
    Look for keywords like "Exclusions", "Ineligible", "0%", or "Not applicable".
    If the answer is not in the context, tell the user you couldn't find it in the current document, but offer to look for related topics.

    <context>
    {context}
    </context>

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    # retriever = vectorstore.as_retriever(
    #     search_type="mmr", 
    #     search_kwargs={"k": 10, "fetch_k": 20}
    # )

    # The Clean LCEL Chain
    rag_chain = (
        {
            "context": retriever | format_docs, 
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain.invoke(question)

def main():
    print("--- User Chat Client ---")
    
    # 1. Setup local storage directory
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)

    # 2. Sync Index
    if not os.path.exists(f"{FOLDER_PATH}/my_faiss.faiss"):
        print("Local index not found.")
        if not load_index_from_s3():
            print("Please run the admin script to upload a PDF first.")
            sys.exit(1)
    else:
        choice = input("Local index found. Sync fresh index from S3? (y/n): ")
        if choice.lower() == 'y':
            load_index_from_s3()

    # 3. Load Vector Store
    try:
        faiss_index = FAISS.load_local(
            index_name="my_faiss",
            folder_path=FOLDER_PATH,
            embeddings=bedrock_embeddings,
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        print(f"Error loading FAISS index: {e}")
        sys.exit(1)

    llm = get_llm()
    print("\n--- System Ready (Nova-Micro) ---")
    print("Type 'quit' or 'exit' to leave.\n")

    while True:
        try:
            question = input("Your Question: ")
            if question.lower() in ["quit", "exit"]:
                break
            
            if not question.strip():
                continue

            print("Thinking...")
            answer = get_response(llm, faiss_index, question)
            print(f"\nAnswer: {answer}\n")
            print("-" * 30)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()