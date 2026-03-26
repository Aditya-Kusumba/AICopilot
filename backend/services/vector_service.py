import chromadb
import uuid

client = chromadb.PersistentClient(path="data/chroma")

def get_collection(name):
    return client.get_or_create_collection(name=name)

def add_documents(collection_name, docs):
    collection = get_collection(collection_name)

    for doc in docs:
        collection.add(
            documents=[doc["summary"]],
            metadatas=[doc],
            ids=[str(uuid.uuid4())]
        )

def get_all_documents(collection_name):
    collection = get_collection(collection_name)
    return collection.get()