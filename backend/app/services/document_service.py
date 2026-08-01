from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.document_chunk import DocumentChunk

from app.repositories.document_repository import DocumentRepository
from app.repositories.chunk_repository import ChunkRepository

from app.services.document_processor import DocumentProcessor
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService

from app.vector_store.milvus import MilvusStore

UPLOAD_DIR = Path("storage/documents")


class DocumentService:

    def __init__(
        self,
        db: Session,
    ):
        self.document_repository = DocumentRepository(db)
        self.chunk_repository = ChunkRepository(db)

        self.processor = DocumentProcessor()
        self.chunker = ChunkingService()
        self.embedder = EmbeddingService()

        self.milvus = MilvusStore()

        self.milvus.create_collection()

    def upload_document(
        self,
        file: UploadFile,
    ) -> Document:

        file_extension = Path(file.filename).suffix

        unique_filename = f"{uuid4()}{file_extension}"

        file_path = UPLOAD_DIR / unique_filename

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        document = Document(
            filename=file.filename,
            file_path=str(file_path),
            status="processing",
        )

        document = self.document_repository.create(document)

        text = self.processor.extract_text(str(file_path))

        chunks = self.chunker.split_text(text)

        chunk_models = []

        for index, chunk in enumerate(chunks):

            chunk_model = DocumentChunk(
                document_id=document.id,
                content=chunk,
                chunk_index=index,
            )

            chunk_models.append(chunk_model)

        saved_chunks = self.chunk_repository.create_many(chunk_models)

        for chunk_model in saved_chunks:

            embedding = self.embedder.create_embedding(chunk_model.content)

            self.milvus.insert_chunk(
                chunk_id=str(chunk_model.id),
                document_id=str(document.id),
                chunk_index=chunk_model.chunk_index,
                embedding=embedding,
            )

        document.status = "processed"

        return document
