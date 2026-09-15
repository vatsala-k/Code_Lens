import faiss
import numpy as np
def create_vector_store(embeddings):
    vectors=np.array(embeddings).astype("float32")
    dimensions=vectors.shape[1]
    index=faiss.IndexFlatL2(dimensions)
    index.add(vectors)
    return index    
