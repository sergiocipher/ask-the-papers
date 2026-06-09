import json
from pathlib import Path

from fastapi import APIRouter, UploadFile
from services.chunk_service import create_chunks_from_pages
from services.pdf_service import extract_pdf_pages

router = APIRouter()

DATA_DIR = "data"
UPLOAD_DIR = "uploads"

Path(DATA_DIR).mkdir(exist_ok=True)
Path(UPLOAD_DIR).mkdir(exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    pages = extract_pdf_pages(file_path)
    chunks = create_chunks_from_pages(pages)

    with open(f"{DATA_DIR}/chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)

    return {
        "total_pages": len(pages),
        "total_chunks": len(chunks)
    }
