import chromadb
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.vectorstores.chroma import Chroma

chroma_db_path = "data/chroma_db"
chroma_collection_name = "youtube_transcripts"
chroma_embedding_model = "all-MiniLM-L6-v2"


def setup_chroma():
    client = chromadb.PersistentClient(path=chroma_db_path)
    client.get_or_create_collection(chroma_collection_name)
    return Chroma(
        client=client,
        collection_name=chroma_collection_name,
        embedding_function=SentenceTransformerEmbeddings(model_name=chroma_embedding_model),
        persist_directory=chroma_db_path
    )


def get_chroma():
    return Chroma(
        collection_name=chroma_collection_name,
        embedding_function=SentenceTransformerEmbeddings(model_name=chroma_embedding_model),
        persist_directory=chroma_db_path
    )
