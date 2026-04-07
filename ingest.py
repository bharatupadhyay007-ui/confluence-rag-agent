from sentence_transformers import SentenceTransformer
import chromadb
from data.remediation_docs import documents

print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Setting up vector database...")
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="remediation_docs",
    metadata={"hnsw:space": "cosine"}
)

print(f"Ingesting {len(documents)} documents...")

for doc in documents:
    print(f"  Processing: {doc['title']}")
    
    embedding = model.encode(doc['content']).tolist()
    
    collection.add(
        ids=[doc['id']],
        embeddings=[embedding],
        documents=[doc['content']],
        metadatas=[{
            "title": doc['title'],
            "category": doc['category'],
            "product": doc['product']
        }]
    )

print(f"\nDone! {len(documents)} documents ingested into vector database.")
print("Vector database saved to ./chroma_db")
