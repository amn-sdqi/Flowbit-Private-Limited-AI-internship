import re


def process_email(text: str) -> dict:
    sender = re.search(r"From:\s*([^\s]+)", text, re.IGNORECASE)
    urgency = "high" if "urgent" in text.lower() else "normal"
    return {
        "sender": sender.group(1) if sender else "unknown",
        "urgency": urgency,
        "content": text,
    }
