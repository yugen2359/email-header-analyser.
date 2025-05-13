from fastapi import FastAPI
from pydantic import BaseModel
from email.parser import Parser

app = FastAPI()

class HeaderInput(BaseModel):
    raw_header: str

@app.post("/analyze")
def analyze_headers(data: HeaderInput):
    headers = Parser().parsestr(data.raw_header)
    return {
        "From": headers.get("From"),
        "To": headers.get("To"),
        "Subject": headers.get("Subject"),
        "SPF": headers.get("Received-SPF", ""),
        "DKIM": headers.get("Authentication-Results", "")
    }
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "✅ FastAPI is live!"}
