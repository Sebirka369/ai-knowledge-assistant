from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


class ChunkRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create_many(
        self,
        chunks: list[DocumentChunk],
    ) -> list[DocumentChunk]:

        self.db.add_all(chunks)
        self.db.commit()

        return chunks

    def get_by_id(
        self,
        chunk_id: int,
    ) -> DocumentChunk | None:

        return self.db.query(DocumentChunk).filter(DocumentChunk.id == chunk_id).first()

    def get_by_ids(
        self,
        chunk_ids: list[int],
    ) -> list[DocumentChunk]:

        if not chunk_ids:
            return []

        return (
            self.db.query(DocumentChunk).filter(DocumentChunk.id.in_(chunk_ids)).all()
        )
