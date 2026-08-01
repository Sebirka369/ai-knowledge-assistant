from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.document_service import DocumentService


def get_document_service(
    db: Session = Depends(get_db),
) -> DocumentService:
    return DocumentService(db)
