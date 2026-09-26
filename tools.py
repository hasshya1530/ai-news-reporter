import requests
from crewai.tools import tool


@tool("AI News Search")
def search_ai_news(topic: str) -> str:
    """
    Search current AI and technology news related to a topic.

    Args:
        topic: The AI or technology topic to search for.
    """

    response = requests.get(
        "https://whatstrending.ai/api/articles",
        params={"limit": 10},
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()
    articles = data.get("data", [])

    relevant_articles = []

    topic_words = [word.lower() for word in topic.split() if len(word) > 2]

    for article in articles:
        searchable_text = " ".join(
            [
                article.get("title", ""),
                article.get("originalTitle", ""),
                article.get("summary", ""),
                article.get("category", ""),
            ]
        ).lower()

        if any(word in searchable_text for word in topic_words):
            relevant_articles.append(article)

    if not relevant_articles:
        relevant_articles = articles

    results = []

    for article in relevant_articles[:5]:
        results.append(
            "\n".join(
                [
                    f"Title: {article.get('title', '')}",
                    f"Source: {article.get('source', '')}",
                    f"Category: {article.get('category', '')}",
                    f"Date: {article.get('date', '')}",
                    f"Summary: {article.get('summary', '')}",
                    f"Link: {article.get('link', '')}",
                ]
            )
        )

    return "\n\n".join(results)
