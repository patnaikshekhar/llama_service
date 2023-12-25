from model import create_pipeline
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

pipeline, token_id = create_pipeline()

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    top_k: int = 1
    max_length: int = 400
    num_return_sequences: int = 1

class ChatResponse(BaseModel):
    messages: List[str]

@app.post("/api/v1/chat")
def chat(request: ChatRequest) -> ChatResponse:

    print("Prediction started....")
    
    sequences = pipeline(
        request.message,
        do_sample=True,
        top_k=request.top_k,
        num_return_sequences=request.num_return_sequences,
        eos_token_id=token_id,
        max_length=request.max_length,
    )

    print("Prediction completed....")

    output = []
    for seq in sequences:
        output.append(seq['generated_text'])

    return {
        "messages": output
    }

    # for seq in sequences:
    #     print(f"{seq['generated_text']}")