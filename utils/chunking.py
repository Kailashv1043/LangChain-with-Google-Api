from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs(documents):
    splitter= RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)