import fitz  # PyMuPDF


class DocumentProcessor:

    def extract_text(self, file_path: str) -> str:
        """
        Extract text from PDF file.
        """

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text