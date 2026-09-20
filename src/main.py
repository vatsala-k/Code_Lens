from file_discovery import discover_files
from file_filter import filter_files
from document_loader import load_documents
from repository_chunker import chunk_documents
from embeddings import create_embeddings
from vector_store import create_vector_store
from retriever import retrieve
from generator import generate_answer


repository_path = "repos/test_repo"
all_files = discover_files(repository_path)
filtered_files = filter_files(all_files)
documents = load_documents(
    filtered_files,
    repository_path
)
chunks = chunk_documents(documents)
embeddings = create_embeddings(chunks)
index = create_vector_store(embeddings)
question = input("\nAsk a question about the repository: ")
retrieved_chunks = retrieve(
    question,
    index,
    chunks,
    create_embeddings,
    k=3
)
answer = generate_answer(
    question,
    retrieved_chunks
)
print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)
print(answer)