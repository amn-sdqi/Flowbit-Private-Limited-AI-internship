from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
from typing import Optional
import uuid

from app.agents.classifier import classify_input
from app.memory.sqlite_store import read_logs # type: ignore
from app.agents.email_agent import process_email
from app.agents.json_agent import process_json

app = FastAPI()



class TextInput(BaseModel):
    text: str
    thread_id: Optional[str] = None


@app.post("/process")
async def process_input(
    file: Optional[UploadFile] = None,
    text: str = Form(default=None),
    thread_id: str = Form(default=None),
):
    content = await file.read() if file else text.encode("utf-8")
    result = classify_input(content)
    
    thread_id = thread_id or str(uuid.uuid4())

    intent = result["log"]["intent"]
    data = {}  # agent chaining output

    if intent in ["Invoice", "Complaint"]:
        email_data = process_email(result["data"]["text"])
        data.update(email_data)
    if intent == "RFQ":
        json_data = process_json({"rfq_text": result["data"]["text"]})
        data.update(json_data)

    if not data:
        data = {"text": result["data"]["text"], "note": "No agent matched"}

    save_log(result["log"], data, thread_id)

    return {"route": intent + " Agent", "data": data}


@app.post("/process-json")
async def process_json_text(payload: TextInput):
    content = payload.text.encode("utf-8")
    result = classify_input(content)
    thread_id = payload.thread_id or str(uuid.uuid4())

    intent = result["log"]["intent"]
    data = {}  # agent chaining output

    if intent in ["Invoice", "Complaint"]:
        email_data = process_email(result["data"]["text"])
        data.update(email_data)
    if intent == "RFQ":
        json_data = process_json({"rfq_text": result["data"]["text"]})
        data.update(json_data)

    if not data:
        data = {"text": result["data"]["text"], "note": "No agent matched"}

    save_log(result["log"], data, thread_id)

    return {"route": intent + " Agent","thread_id":thread_id, "data": data}


@app.get("/logs")
def get_logs():
    return {"logs": read_logs()}
