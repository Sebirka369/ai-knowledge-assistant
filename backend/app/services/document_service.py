from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.document_repository import DocumentRepository


UPLOAD_DIR = Path("storage/documents")


class DocumentService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = DocumentRepository(db)


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
            status="uploaded",
        )


        return self.repository.create(document)