from crewai import Crew, Process

from agents import create_agents
from tasks import create_tasks
from tools import search_ai_news


def get_research(topic: str) -> str:
    """Fetch current news articles for the requested topic."""
    return search_ai_news.run(topic)


def generate_article(
    topic: str,
    research: str,
    article_style: str,
    article_length: str,
) -> str:
    """Generate an article using the retrieved research."""

    # Create fresh agents for this request.
    news_researcher, news_writer = create_agents()

    # Create fresh tasks using the new agents.
    research_task, write_task = create_tasks(
        news_researcher,
        news_writer,
    )

    # Create a fresh Crew for this request.
    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff(
        inputs={
            "topic": topic,
            "research": research,
            "article_style": article_style,
            "article_length": article_length,
        }
    )

    return str(result)


if __name__ == "__main__":
    topic = input("Enter a topic: ").strip()

    if not topic:
        print("Please enter a topic.")
    else:
        article_style = input(
            "Enter article style (News Report / Research Brief / Explainer): "
        ).strip()

        article_length = input(
            "Enter article length (Short / Medium / Detailed): "
        ).strip()

        print("\n===== RESEARCH =====\n")

        research = get_research(topic)
        print(research)

        print("\n===== GENERATING ARTICLE =====\n")

        article = generate_article(
            topic=topic,
            research=research,
            article_style=article_style,
            article_length=article_length,
        )

        print("\n===== FINAL NEWS ARTICLE =====\n")
        print(article)
