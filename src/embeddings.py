import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def create_embeddings(chunks):
    texts=[chunk["text"] for chunk in chunks]
    response=client.models.embed_content( model='gemini-embedding-001',contents=texts)
    embeddings=[embedding.values for embedding in response.embeddings]
    return embeddings
if __name__ == "__main__":

    from file_discovery import discover_files
    from file_filter import filter_files
    from document_loader import load_documents
    from repository_chunker import chunk_documents

    repository_path = "repos/test_repo"

    all_files = discover_files(repository_path)
    filtered_files = filter_files(all_files)

    documents = load_documents(
        filtered_files,
        repository_path
    )

    chunks = chunk_documents(documents)

    embeddings = create_embeddings(chunks)

    print(f"\nChunks: {len(chunks)}")
    print(f"Embeddings: {len(embeddings)}")
    print(f"Embedding dimension: {len(embeddings[0])}")