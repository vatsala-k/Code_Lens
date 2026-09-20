from pathlib import Path
def load_documents(files, repository_path):
    documents=[]
    repository_path=Path(repository_path)
    for file in files:
        file=Path(file)
        try:
            text=file.read_text(encoding="utf 8")
        except UnicodeDecodeError:
            print(f"Skipping non text file: {file}")
            continue
        relative_path=file.relative_to(repository_path)
        document={
            "text": text,
            "file_path": str(relative_path),
            "file_type": file.suffix.lower(),
            "repository": repository_path.name
        }
        documents.append(document)

    return documents
if __name__=="__main__":
    from file_discovery import discover_files
    from file_filter import filter_files
    repository_path="repos/test_repo"
    all_files=discover_files(repository_path)
    filtered_files=filter_files(all_files)
    documents=load_documents(filtered_files,repository_path)
    print(f"\nLoaded {len(documents)} documents\n")

    for document in documents:
        print("="*50)
        print("File:",document["file_path"])
        print("Type:", document["file_type"])
        print("Repository:", document["repository"])

        print("\nContent preview:")
        print(document["text"][:300])

