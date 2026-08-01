from app.services.llm_service import LLMService


service = LLMService()

question = "What is Python?"

context = """
Python is a high-level programming language.
It is widely used for backend development, automation,
data science, and artificial intelligence.
"""

answer = service.generate(
    question=question,
    context=context,
)

print("Question:")
print(question)

print("\nAnswer:")
print(answer)
