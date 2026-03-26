from fastapi import APIRouter
from models.schemas import ActionRequest, CitationRequest
from services.vector_service import get_all_documents
from services.llm_service import (
    generate_literature_review,
    generate_research_gap,
    generate_citations
)
from services.pdf_service import generate_gap_pdf

router = APIRouter()


@router.post("/literature")
def literature(req: ActionRequest):
    collection_name = f"chat_{req.chat_id}"

    docs = get_all_documents(collection_name)
    texts = docs["documents"]

    review = generate_literature_review(texts)

    return {"literature_review": review}


@router.post("/research-gap")
def research_gap(req: ActionRequest):
    collection_name = f"chat_{req.chat_id}"

    docs = get_all_documents(collection_name)

    papers = docs["metadatas"]
    texts = docs["documents"]

    gaps = []

    for i in range(len(texts)):
        gap = generate_research_gap(texts[i])

        gaps.append({
            "title": papers[i]["title"],
            "gap": gap
        })

    pdf_path = generate_gap_pdf(gaps)

    return {"pdf_path": pdf_path}


@router.post("/citation")
def citation(req: CitationRequest):
    collection_name = f"chat_{req.chat_id}"

    docs = get_all_documents(collection_name)
    papers = docs["metadatas"]

    citations = generate_citations(papers, req.style)

    return {"citations": citations}