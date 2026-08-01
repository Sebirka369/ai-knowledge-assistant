from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_embedding(
        self,
        text: str,
    ) -> list[float]:
        """
        Convert text into a vector embedding.
        """

        embedding = self.model.encode(text)

        return embedding.tolist()
