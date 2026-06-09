from fastapi import APIRouter
from services.paper_services import search_papers

router = APIRouter()


@router.get("/papers/search")
def search(query: str):
    return search_papers(query)
