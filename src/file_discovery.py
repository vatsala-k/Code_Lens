from pathlib import Path
def discover_files(repository_path):
    repository_path=Path(repository_path)
    files=[]
    for path in repository_path.rglob("*"):
        if path.is_file():
            files.append(path)
    return files
if __name__=="__main__":
    repository_path="repos/test_repo"
    files=discover_files(repository_path)
    print(f"\nFound {len(files)} files :\n")
    for file in files:
        print(file)

    