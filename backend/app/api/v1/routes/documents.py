from fastapi import APIRouter, Depends, UploadFile, File

from app.dependencies.document import get_document_service
from app.services.document_service import DocumentService

router = APIRouter(
    tags=["Documents"],
)


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    service: DocumentService = Depends(get_document_service),
):
    document = service.upload_document(file)

    return {
        "id": document.id,
        "filename": document.filename,
        "status": document.status,
    }
