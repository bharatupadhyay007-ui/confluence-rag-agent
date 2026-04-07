from sentence_transformers import SentenceTransformer
import chromadb
import requests

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="remediation_docs",
    metadata={"hnsw:space": "cosine"}
)

def ask_agent(question):
    print(f"\nQuestion: {question}")
    print("Finding relevant Confluence pages...")

    question_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    context = ""
    sources = []

    for i, (doc, metadata) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0]
    )):
        context += f"\n\nCONFLUENCE PAGE {i+1}: {metadata['title']}\n{doc}"
        sources.append(metadata['title'])
        print(f"  Found: {metadata['title']}")

    prompt = f"""You are an expert banking remediation analyst.
You have access to the following Confluence pages from the Remediation Readiness space:
{context}

Based ONLY on the information in these Confluence pages, answer this question:
{question}

If the answer is not in the Confluence pages, say "I could not find this information in the Remediation Readiness documentation."

Be specific and cite figures and details from the pages where possible.
"""

    print("Sending to LLaMA...")
    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    return {
        "answer": answer,
        "sources": sources
    }

if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == "exit":
            break
        
        result = ask_agent(question)
        
        print("\n--- ANSWER ---")
        print(result["answer"])
        print("\n--- SOURCES ---")
        for source in result["sources"]:
            print(f"  - {source}")
