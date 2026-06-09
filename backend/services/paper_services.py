import arxiv


def search_papers(query: str):

    search = arxiv.Search(
        query=query,
        max_results=10,
        sort_by=arxiv.SortCriterion.Relevance
    )
    client = arxiv.Client()

    papers = []

    for result in client.results(search):

        papers.append(
            {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "summary": result.summary,
                "published": str(result.published),
                "pdf_url": result.pdf_url
            }
        )

    return papers
