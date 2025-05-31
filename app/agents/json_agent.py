def process_json(payload: dict) -> dict:
    required_fields = ["id", "amount", "date"]
    anomalies = [field for field in required_fields if field not in payload]
    return {"normalized": payload, "anomalies": anomalies}
