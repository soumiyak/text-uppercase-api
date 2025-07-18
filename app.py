from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/uppercase")
async def to_uppercase(input: TextInput):
    return {"result": input.text.upper()}
