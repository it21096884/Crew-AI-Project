from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
    "The article must contain approximately {word_count} words."
  ),
  expected_output='A {word_count}-word article on {topic} advancements written in paragraph format.',
  tools=[tool],
  agent=news_writer,
  async_execution=False
)
