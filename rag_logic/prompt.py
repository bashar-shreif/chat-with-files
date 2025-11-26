def prepare_prompt(query, retrieved_chunks):
    context = ""
    for i, chunk in enumerate(retrieved_chunks):
        context = context + f"\n\n[Context {i + 1}]:\n{chunk}"

    prompt = f"""
    You are an AI assistant that answers questions using information extracted from a PDF document.
    Context:
    {context}

    Question:
    {query}

    Instructions:
    - Answer using ONLY the information available in the PDF context above.
    - If the PDF does not contain enough information to answer the question, say so clearly.
    - Be concise, accurate, and specific.
    - Cite the section or page number from the PDF when referencing information, if available.
    - Do not make up any information that is not present in the PDF.

    Answer:
    """

    return prompt
