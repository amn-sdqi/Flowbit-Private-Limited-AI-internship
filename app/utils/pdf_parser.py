from pdfminer.high_level import extract_text
from typing import Union
import io


def extract_pdf_text(file_content: Union[bytes, io.BytesIO]) -> str:
    try:
        if isinstance(file_content, bytes):
            file_content = io.BytesIO(file_content)
        return extract_text(file_content) # type: ignore
    except Exception as e:
        return f"Error reading PDF: {e}"
