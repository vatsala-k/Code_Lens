import subprocess
from pathlib import Path
def clone_repository(repo_url,destination):
    subprocess.run(
        ["git","clone",repo_url,destination],check=True
    )
    return Path(destination)

if __name__ == "__main__":
    repo_url=input("Enter Github Repository Link here: ")
    repository_path=clone_repository(repo_url,"repos/test_repo")
    print(f"Repository cloned to: {repository_path}")




