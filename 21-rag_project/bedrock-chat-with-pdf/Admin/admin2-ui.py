import boto3
import streamlit as st
import os
import uuid

## s3_client
s3_client = boto3.client("s3")
BUCKET_NAME = os.getenv("BUCKET_NAME")

## Bedrock
from langchain_community.embeddings import BedrockEmbeddings

## Text Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

## Pdf Loader
from langchain_community.document_loaders import PyPDFLoader

## import FAISS
from langchain_community.vectorstores import FAISS

bedrock_client = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0", client=bedrock_client)

def get_unique_id():
    return str(uuid.uuid4())


## Split the pages / text into chunks
def split_text(pages, chunk_size, chunk_overlap):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(pages)
    return docs

## create vector store
def create_vector_store(request_id, documents):
    vectorstore_faiss=FAISS.from_documents(documents, bedrock_embeddings)
    file_name=f"{request_id}.bin"
    folder_path="/tmp/"
    vectorstore_faiss.save_local(index_name=file_name, folder_path=folder_path)

    ## upload to S3
    s3_client.upload_file(Filename=folder_path + "/" + file_name + ".faiss", Bucket=BUCKET_NAME, Key="my_faiss.faiss")
    s3_client.upload_file(Filename=folder_path + "/" + file_name + ".pkl", Bucket=BUCKET_NAME, Key="my_faiss.pkl")

    return True

## main method
def main():
    # Page configuration
    st.set_page_config(
        page_title="Chat with PDF Admin",
        page_icon="📚",
        layout="wide",
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #4257B2;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #6C757D;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-message {
        background-color: #D4EDDA;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
    }
    .error-message {
        background-color: #F8D7DA;
        color: #721C24;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
    }
    .info-card {
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 4px solid #4257B2;
    }
    .document-preview {
        background-color: #F8F9FA;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #DEE2E6;
        max-height: 300px;
        overflow-y: auto;
        margin: 1rem 0;
    }
    .upload-box {
        border: 2px dashed #4257B2;
        border-radius: 0.5rem;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
    .pdf-icon {
        font-size: 4rem;
        color: #4257B2;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        color: #6C757D;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #DEE2E6;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("<h1 class='main-header'>📚 Chat with PDF Admin Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Upload and process PDFs for the chat application</p>", unsafe_allow_html=True)
    
    # Create a clean layout
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.subheader("📤 Upload PDF Document")
        st.write("Select a PDF file to process and create a vector store for the chat application.")
        
        st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
        st.markdown("<div class='pdf-icon'>📄</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Optional parameter configuration
        with st.expander("⚙️ Advanced Configuration"):
            chunk_size = st.slider("Chunk Size", min_value=100, max_value=2000, value=1000, step=100, 
                                help="Size of each text chunk for processing")
            chunk_overlap = st.slider("Chunk Overlap", min_value=0, max_value=500, value=200, step=50, 
                                    help="Overlap between consecutive chunks")
            
            st.info("""
            **Configuration Guide:**
            - **Chunk Size**: Larger chunks include more context but may be less specific
            - **Chunk Overlap**: Higher overlap helps maintain context between chunks
            """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Processing section
    with col2:
        if uploaded_file is not None:
            st.markdown("<div class='info-card'>", unsafe_allow_html=True)
            request_id = get_unique_id()
            st.info(f"Processing PDF with Request ID: `{request_id}`")
            
            # Save the uploaded file
            saved_file_name = f"{request_id}.pdf"
            with open(saved_file_name, mode="wb") as w:
                w.write(uploaded_file.getvalue())
            
            # Process with progress indicators
            progress_placeholder = st.empty()
            progress_bar = st.progress(0)
            
            # Step 1: Load PDF
            progress_placeholder.text("📂 Loading PDF document...")
            loader = PyPDFLoader(saved_file_name)
            pages = loader.load_and_split()
            progress_bar.progress(33)
            st.success(f"✅ Successfully loaded {len(pages)} pages")
            
            # Step 2: Split into chunks
            progress_placeholder.text("✂️ Splitting document into chunks...")
            splitted_docs = split_text(pages, chunk_size, chunk_overlap)
            progress_bar.progress(66)
            st.success(f"✅ Document split into {len(splitted_docs)} chunks")
            
            # Step 3: Create vector store
            progress_placeholder.text("🔄 Creating vector store and uploading to S3...")
            try:
                result = create_vector_store(request_id, splitted_docs)
                progress_bar.progress(100)
                if result:
                    progress_placeholder.empty()
                    st.markdown("<div class='success-message'>🎉 PDF processed successfully! Vector store created and uploaded to S3.</div>", unsafe_allow_html=True)
                else:
                    progress_placeholder.empty()
                    st.markdown("<div class='error-message'>❌ Error processing PDF. Please check the logs.</div>", unsafe_allow_html=True)
            except Exception as e:
                progress_placeholder.empty()
                st.markdown(f"<div class='error-message'>❌ Error: {str(e)}</div>", unsafe_allow_html=True)
            
            # Document statistics
            if 'result' in locals() and result:
                st.subheader("📊 Document Statistics")
                col_stats1, col_stats2, col_stats3 = st.columns(3)
                with col_stats1:
                    st.metric("Total Pages", len(pages))
                with col_stats2:
                    st.metric("Total Chunks", len(splitted_docs))
                with col_stats3:
                    avg_words = int(sum(len(doc.page_content.split()) for doc in splitted_docs) / max(1, len(splitted_docs)))
                    st.metric("Avg. Words per Chunk", avg_words)
                
                # Display first two chunks as a preview
                st.subheader("👁️ Document Preview")
                tab1, tab2 = st.tabs(["Chunk 1", "Chunk 2"])
                with tab1:
                    st.markdown("<div class='document-preview'>", unsafe_allow_html=True)
                    st.write(splitted_docs[0])
                    st.markdown("</div>", unsafe_allow_html=True)
                with tab2:
                    st.markdown("<div class='document-preview'>", unsafe_allow_html=True)
                    st.write(splitted_docs[1])
                    st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='info-card' style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<div class='pdf-icon'>📄</div>", unsafe_allow_html=True)
            st.write("👈 Please upload a PDF file to start processing")
            st.write("This application processes PDFs and creates vector stores for the Chat with PDF feature.")
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("<div class='footer'>Chat with PDF Admin Portal | Powered by LangChain & FAISS</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()