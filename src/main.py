from loader import load_document
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import create_vector_store
from retriever import retrieve
from generator import generate_answer

document=load_document("data/code_base.txt")
chunks=chunk_text(document)
embeddings=create_embeddings(chunks)
index=create_vector_store(embeddings)
question=input("Ask a question: ")
retrieved_chunks=retrieve(question,index,chunks,create_embeddings)
answer=generate_answer(question,retrieved_chunks)
print("\nAnswer:")
print(answer)