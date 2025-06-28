from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Call the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies and trends in {topic} and summarize key insights concisely.",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity and analytical rigor, you're at the forefront of innovation. "
        "You explore emerging trends and evaluate their pros, cons, market opportunities, and risks "
        "to support insightful content creation."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a writing agent responsible for writing news blogs
news_writer = Agent(
    role="Writer",
    goal="Narrate engaging and positive tech stories about {topic} in approximately {word_count} words.",
    verbose=True,
    memory=True,
    backstory=(
        "With a talent for simplifying complex ideas, you create clear and captivating articles "
        "that resonate with readers. Your writing is structured in well-formed paragraphs, making "
        "technical advancements accessible and exciting."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
