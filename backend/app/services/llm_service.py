import requests


class LLMService:

    def __init__(
        self,
        ollama_url: str = "http://localhost:11434",
        model: str = "llama3:latest",
    ):
        self.ollama_url = ollama_url
        self.model = model

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:

        prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        response = requests.post(
            f"{self.ollama_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
        )

        response.raise_for_status()

        return response.json()["response"]
