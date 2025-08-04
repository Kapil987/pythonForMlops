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
        return True
    except s3_client.exceptions.ClientError as e:
        error_code = e.response["Error"]["Code"]
        if error_code == "404":
            st.error("Index files not found in S3. Please verify the files exist or generate/upload them.")
        else:
            st.error("Error downloading index files: " + str(e))
        return False

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
    # Page configuration
    st.set_page_config(
        page_title="Chat with PDF",
        page_icon="📚",
        layout="centered"
    )
    
    # Dark theme CSS
    st.markdown("""
    <style>
    /* Dark theme for entire app */
    .stApp {
        background-color: #1E1E2E;
        color: #CDD6F4;
    }
    
    /* Main container - ensure dark background */
    section[data-testid="stSidebar"] {
        background-color: #181825;
        border-right: 1px solid #313244;
    }
    
    div[data-testid="stVerticalBlock"] {
        background-color: #1E1E2E;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: #CBA6F7 !important;
        text-align: center;
    }
    
    /* Status messages */
    .status-message {
        background-color: #313244;
        color: #A6E3A1;
        border-radius: 8px;
        padding: 10px;
        margin: 10px 0;
        text-align: center;
    }
    
    .error-message {
        background-color: #313244;
        color: #F38BA8;
        border-radius: 8px;
        padding: 10px;
        margin: 10px 0;
        text-align: center;
    }
    
    /* Chat messages */
    .user-message {
        background-color: #74C7EC;
        color: #1E1E2E;
        border-radius: 18px 18px 0 18px;
        padding: 12px 16px;
        margin: 8px 0;
        max-width: 80%;
        margin-left: auto;
        text-align: right;
        word-wrap: break-word;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    .ai-message {
        background-color: #313244;
        color: #CDD6F4;
        border-radius: 18px 18px 18px 0;
        padding: 12px 16px;
        margin: 8px 0;
        max-width: 80%;
        text-align: left;
        word-wrap: break-word;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    /* Input area styling */
    .stTextInput > div {
        background-color: #313244;
        border-radius: 24px;
    }
    
    .stTextInput > div > div > input {
        background-color: #313244;
        color: #CDD6F4;
        border-radius: 24px;
        padding: 10px 15px;
        border: 1px solid #45475A;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #6C7086;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #74C7EC;
        color: #1E1E2E;
        font-weight: bold;
        border-radius: 24px;
        border: none;
        padding: 4px 15px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #89DCEB;
        color: #1E1E2E;
    }
    
    /* Clear chat button */
    .clear-button > button {
        background-color: #313244;
        color: #CDD6F4;
        border: 1px solid #45475A;
    }
    
    .clear-button > button:hover {
        background-color: #45475A;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #6C7086;
        padding-top: 10px;
        border-top: 1px solid #313244;
    }
    
    /* Spinner color */
    .stSpinner > div > div {
        border-top-color: #CBA6F7 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # App header
    st.markdown("<h1>📚 Chat with PDF</h1>", unsafe_allow_html=True)
    
    # System status (hidden once loaded)
    status_container = st.empty()
    
    with status_container.container():
        with st.spinner("Loading document index..."):
            index_loaded = load_index()
            
        if not index_loaded:
            st.markdown('<div class="error-message">⚠️ Failed to load document index. Please check your connection and try again.</div>', unsafe_allow_html=True)
            st.stop()
    
    # Load FAISS index
    try:
        faiss_index = FAISS.load_local(
            index_name="my_faiss",
            folder_path=folder_path,
            embeddings=bedrock_embeddings,
            allow_dangerous_deserialization=True
        )
        status_container.empty()  # Clear the status area once loaded
    except Exception as e:
        st.markdown(f'<div class="error-message">⚠️ Failed to load FAISS index: {str(e)}</div>', unsafe_allow_html=True)
        st.stop()
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Chat container
    chat_container = st.container()
    
    # Display chat history
    with chat_container:
        if not st.session_state.chat_history:
            st.markdown('<div class="status-message">💬 Ask a question about your PDF document</div>', unsafe_allow_html=True)
        else:
            for q, a in st.session_state.chat_history:
                st.markdown(f'<div class="user-message">{q}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="ai-message">{a}</div>', unsafe_allow_html=True)
    
    # Input area at the bottom
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Two-column layout for input and send button
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input("", placeholder="Ask about your document...", label_visibility="collapsed", key="user_question")
    
    with col2:
        send_button = st.button("Send", type="primary", use_container_width=True)
    
    # Process user input
    if send_button and user_input.strip():
        with st.spinner("Processing..."):
            llm = get_llm()
            response = get_response(llm, faiss_index, user_input)
            st.session_state.chat_history.append((user_input, response))
        st.rerun()
    
    # Clear chat button (styled differently)
    if st.session_state.chat_history:
        st.markdown('<div class="clear-button">', unsafe_allow_html=True)
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="footer">Powered by AWS Bedrock & LangChain</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()