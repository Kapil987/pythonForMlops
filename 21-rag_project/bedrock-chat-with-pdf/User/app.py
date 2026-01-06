import boto3
import streamlit as st
import os
# from operator import itemgetter

from langchain_aws import BedrockEmbeddings
# ChatBedrock for Titan Premier/Nova
from langchain_aws import ChatBedrock 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS

## AWS Setup
REGION = "us-east-1"
s3_client = boto3.client("s3", region_name=REGION)
bedrock_client = boto3.client(service_name="bedrock-runtime", region_name=REGION)

BUCKET_NAME = os.getenv("BUCKET_NAME")
folder_path = "/tmp"

## Initialize Embeddings (Keep Titan Embed for vector search)
bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0", 
    client=bedrock_client
)

def load_index():
    s3_client.download_file(Bucket=BUCKET_NAME, Key="my_faiss.faiss", Filename=f"{folder_path}/my_faiss.faiss")
    s3_client.download_file(Bucket=BUCKET_NAME, Key="my_faiss.pkl", Filename=f"{folder_path}/my_faiss.pkl")

def get_llm():
    # CHANGE: Switched to ChatBedrock
    return ChatBedrock(
        model_id="us.amazon.nova-micro-v1:0", 
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
    st.set_page_config("Client - Chat with PDF")
    st.header("Chat with your PDF (Bedrock + RAG)")

    if st.button("Download/Sync Index from S3"):
        try:
            with st.spinner("Fetching latest index..."):
                load_index()
                st.success("Index synced!")
        except Exception as e:
            st.error(f"Failed to find index in S3. Error: {e}")

    if os.path.exists(f"{folder_path}/my_faiss.faiss"):
        faiss_index = FAISS.load_local(
            index_name="my_faiss",
            folder_path=folder_path,
            embeddings=bedrock_embeddings,
            allow_dangerous_deserialization=True
        )
        st.info("Knowledge Base is Ready.")

        question = st.text_input("Ask a question about your document:")
        if st.button("Ask Bedrock"):
            if question:
                with st.spinner("Thinking..."):
                    llm = get_llm()
                    answer = get_response(llm, faiss_index, question)
                    st.markdown("### Answer:")
                    st.write(answer)
            else:
                st.warning("Please enter a question first.")
    else:
        st.warning("No index found locally. Please click 'Download/Sync Index' above.")

if __name__ == "__main__":
    main()