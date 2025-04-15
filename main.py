from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv

CSV_FILE = "sensors.csv"

class Sensor(BaseModel):
    id: str
    name: str
    value: float
    timestamp: str

def init_csv():
    try:
        with open(CSV_FILE, 'x', newline="") as file:
            write = csv.writer(file)
            write.writerow(["id", "name", "value", "timestamp"])
    except FileExistsError:
        pass

init_csv()

def read_sensors():
    with open(CSV_FILE, mode="r") as file:
        read = csv.DictReader(file)
        return [row for row in read]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sensors")
def get_sensors():
    return read_sensors()

