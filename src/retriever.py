import numpy as np
def retrieve(question, index, chunks,create_embeddings, k=3):
    question_embedding=create_embeddings([{"text":question}])[0]
    query_vector=np.array([question_embedding]).astype("float32")
    distances, indices=index.search(query_vector,k)
    retrieved_chunks=[]
    for i in indices[0]:
        retrieved_chunks.append(chunks[i])
    return retrieved_chunks
#testing
if __name__ == "__main__":

    from file_discovery import discover_files
    from file_filter import filter_files
    from document_loader import load_documents
    from repository_chunker import chunk_documents
    from embeddings import create_embeddings
    from vector_store import create_vector_store

    repository_path = "repos/test_repo"

    # Discover files
    all_files = discover_files(repository_path)

    # Filter files
    filtered_files = filter_files(all_files)

    # Load documents
    documents = load_documents(
        filtered_files,
        repository_path
    )

    # Create chunks
    chunks = chunk_documents(documents)

    # Create embeddings
    embeddings = create_embeddings(chunks)

    # Create FAISS index
    index = create_vector_store(embeddings)

    # Ask a question
    question = "How does the Player class work?"

    # Retrieve relevant chunks
    retrieved_chunks = retrieve(
        question,
        index,
        chunks,
        create_embeddings,
        k=3
    )

    print("\nQuestion:")
    print(question)

    print("\nRetrieved chunks:\n")

    for chunk in retrieved_chunks:

        print("=" * 60)

        print("File:", chunk["file_path"])
        print("Type:", chunk["file_type"])
        print("Chunk ID:", chunk["chunk_id"])

        print("\nContent:")
        print(chunk["text"][:500])