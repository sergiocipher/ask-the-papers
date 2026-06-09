def chunk_text(text: str, chunk_size: int = 500):
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])

        chunks.append(chunk)

    return chunks


def create_chunks_from_pages(pages):
    chunks = []

    chunk_counter = 1

    for page in pages:
        page_chunks = chunk_text(page["content"])

        for chunk in page_chunks:
            chunks.append(
                {
                    "chunk_id": f"chunk_{chunk_counter}",
                    "page_number": page["page_number"],
                    "content": chunk
                }
            )

            chunk_counter += 1

    return chunks
