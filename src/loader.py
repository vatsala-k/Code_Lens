def load_document(path):
    with open(path,"r") as file:
        text=file.read()

    return text
