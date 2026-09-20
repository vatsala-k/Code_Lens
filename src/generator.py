import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question, retrieved_chunks):

    context = ""

    for chunk in retrieved_chunks:

        context += f"""
File: {chunk["file_path"]}
Chunk: {chunk["chunk_id"]}

{chunk["text"]}

"""

    prompt = f"""
You are Code_Lens, an AI assistant that answers questions
about software repositories.

Answer the user's question using ONLY the provided repository context.

If the answer cannot be found in the provided context,
say that the information is not available in the retrieved code.

When useful, mention the file name where the information was found.

Repository context:

{context}

User question:

{question}
"""

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text