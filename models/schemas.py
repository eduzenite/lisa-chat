from pydantic import BaseModel

class RequestSchema(BaseModel):
    input_text: str

class ResponseSchema(BaseModel):
    prediction: str
