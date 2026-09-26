from agents import news_researcher
from tasks import research_task

result = news_researcher.execute_task(task=research_task)

print("\n===== RESEARCH RESULT =====\n")
print(result)
