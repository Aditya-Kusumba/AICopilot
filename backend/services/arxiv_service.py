import arxiv

def fetch_papers(query: str, max_results: int):
    print(f"Fetching papers for query: {query} with max_results: {max_results}")
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "authors": [a.name for a in result.authors],
            "pdf_url": result.pdf_url
        })

    return papers