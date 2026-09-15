def chunk_text(text, chunk_size=500):
    chunk=[]
    for i in range(0, len(text),chunk_size):
        chunk.append(text[i:i+chunk_size])
    return chunk