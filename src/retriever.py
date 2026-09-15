import numpy as np
def retrieve(question, index, chunks,create_embeddings, k=3):
    question_embedding=create_embeddings([question])[0]
    query_vector=np.array([question_embedding]).astype("float32")
    distances, indices=index.search(query_vector,k)
    retrieved_chunks=[]
    for i in indices[0]:
        retrieved_chunks.append(chunks[i])
    return retrieved_chunks
