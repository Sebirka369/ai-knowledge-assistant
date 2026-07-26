from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


class ChunkRepository:

    def __init__(self, db: Session):
        self.db = db


    def create_many(
        self,
        chunks: list[DocumentChunk],
    ) -> list[DocumentChunk]:

        self.db.add_all(chunks)
        self.db.commit()

        return chunks