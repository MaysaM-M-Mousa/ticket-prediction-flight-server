from fastapi import FastAPI
from model.logic import pipe
from pydantic import BaseModel

app = FastAPI()


class Record(BaseModel):
    MktCoupons: int
    Quarter: int
    Origin: str
    Dest: str
    ContiguousUSA: float
    NumTicketsOrdered: int
    AirlineCompany: str


@app.get("/")
def sayHi():
    return {"message": "Hello Maysam :)"}


@app.post("/ticket/predict")
def predict(record: Record):
    return {'prediction': pipe(dict(record))[0]}
