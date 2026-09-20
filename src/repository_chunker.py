def chunk_documents(documents, chunk_size=500):
    chunks=[]
    for document in documents:
        text=document["text"]
        for i in range(0,len(text),chunk_size):
            chunk_text=text[i:i+chunk_size]
            chunk={
                "text":chunk_text,
                "file_path": document["file_path"],
                "file_type":document["file_type"],
                "repository":document["repository"],
                "chunk_id":i//chunk_size
            }
            chunks.append(chunk)
    return chunks

if __name__=="__main__":
    from file_discovery import discover_files
    from file_filter import filter_files
    from document_loader import load_documents

    repository_path="repos/test_repo"
    all_files=discover_files(repository_path)
    filtered_files=filter_files(all_files)
    documents=load_documents(filtered_files,repository_path)
    chunks=chunk_documents(documents)
    print(f"\n Documents: {len(documents)}")
    print(f"\n Chunks: {len(chunks)}")

    for chunk in chunks[:5]:
        print("="*50)
        print("File:", chunk["file_path"])
        print("Type:", chunk["file_type"])
        print("Chunk ID:", chunk["chunk_id"])
        print("\nContent:")
        print(chunk["text"][:300])
