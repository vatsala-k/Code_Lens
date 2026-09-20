import faiss
import numpy as np
def create_vector_store(embeddings):
    vectors=np.array(embeddings).astype("float32")
    dimensions=vectors.shape[1]
    index=faiss.IndexFlatL2(dimensions)
    index.add(vectors)
    return index    

# testing
if __name__ == "__main__":

    from file_discovery import discover_files
    from file_filter import filter_files
    from document_loader import load_documents
    from repository_chunker import chunk_documents
    from embeddings import create_embeddings

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

    print("\nDocuments:", len(documents))
    print("Chunks:", len(chunks))
    print("Embeddings:", len(embeddings))
    print("FAISS vectors:", index.ntotal)