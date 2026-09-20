from pathlib import Path
IGNORED_DIRECTORIES = {
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    "libraries"
}


ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".xml",
    ".html",
    ".css",
    ".scss",
    ".sql",
    ".sh",
}

def filter_files(files):
    filtered_files=[]
    for file in files:
        path=Path(file)
        if any(directory in IGNORED_DIRECTORIES for directory in path.parts):
            continue
        filtered_files.append(path)
    return filtered_files

if __name__=="__main__":
    from file_discovery import discover_files
    repository_path="repos/test_repo"
    all_files=discover_files(repository_path)
    filtered_files=filter_files(all_files)
    print(f"Total number of files found {len(all_files)}")
    print(f"Total number of useful files {len(filtered_files)}")

    for file in filtered_files:
        print(file)
