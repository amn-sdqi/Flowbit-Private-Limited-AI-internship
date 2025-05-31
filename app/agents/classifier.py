from app.utils.pdf_parser import extract_pdf_text
from app.llm.intent_classifier import get_intent
from typing import Dict, Union


def classify_input(content: Union[bytes, str, bytearray, memoryview]) -> Dict:
    if isinstance(content, (bytes, bytearray, memoryview)):
        try:
            content_str = content.decode("utf-8") # type: ignore
            format_type = "Text"
        except UnicodeDecodeError:
            content_str = extract_pdf_text(content)
            format_type = "PDF"
    else:
        content_str = content
        format_type = "Text"

    intent = get_intent(content_str)
    return {
        "route": intent + " Agent",
        "data": {"text": content_str},
        "log": {"format": format_type, "intent": intent},
    }
