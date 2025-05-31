import requests

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
HEADERS = {
    "Authorization": "Bearer {hf_token}",
}

INTENT_LABELS = ["Invoice", "RFQ", "Complaint", "Regulation"]


def get_intent(text: str) -> str:
    payload = {"inputs": text[:1000], "parameters": {"candidate_labels": INTENT_LABELS}}
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result["labels"][0] if result["scores"][0] > 0.5 else "Unknown"
    except Exception as e:
        print(f"Hugging Face API error: {e}")
        return "Unknown"
