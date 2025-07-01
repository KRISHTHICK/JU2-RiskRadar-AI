from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.llms.ollama import Ollama
import tempfile

def query_uploaded_docs(query, pdfs):
    all_docs = []
    for pdf in pdfs:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf.read())
            loader = PyPDFLoader(tmp.name)
            docs = loader.load()
            all_docs.extend(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(all_docs, embeddings)
    retriever = vector_store.as_retriever()
    llm = Ollama(model="tinyllama")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)
