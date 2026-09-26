import os

from crewai import Agent
from crewai.llms.base_llm import BaseLLM
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GemmaLLM(BaseLLM):
    def __init__(self):
        super().__init__(
            model="gemma-4-26b-a4b-it",
            temperature=0.5,
        )

        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    def call(
        self,
        messages,
        callbacks=None,
        available_functions=None,
        **kwargs,
    ) -> str:
        if isinstance(messages, list):
            prompt = "\n".join(
                message.get("content", "")
                for message in messages
                if isinstance(message, dict)
            )
        else:
            prompt = str(messages)

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text or ""


def create_agents():
    """Create fresh CrewAI agents for each article generation request."""

    llm = GemmaLLM()

    news_researcher = Agent(
        role="Senior AI News Researcher",
        goal=(
            "Prepare a factual and source-grounded research brief "
            "about {topic} using only the provided research."
        ),
        backstory=(
            "You are an experienced technology journalist and researcher. "
            "You investigate AI developments carefully, identify important "
            "facts, distinguish facts from inference, and provide reliable "
            "information that can be used to create a clear and informative "
            "technology article."
        ),
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    news_writer = Agent(
        role="AI Technology News Writer",
        goal=(
            "Transform research findings about {topic} into a clear, "
            "accurate, and engaging technology news article."
        ),
        backstory=(
            "You are an experienced technology journalist who specializes "
            "in explaining complex AI developments in a way that is accessible "
            "to a broad audience. You rely only on the research provided to "
            "you and avoid inventing facts or unsupported claims."
        ),
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    return news_researcher, news_writer
