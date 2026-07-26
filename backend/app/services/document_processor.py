from pathlib import Path


class DocumentProcessor:

    def extract_text(self, file_path: str) -> str:
        """
        Extract text from document.
        """

        path = Path(file_path)

        return path.read_text()