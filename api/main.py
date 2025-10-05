from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from Calculationsmain import calculate_aqi
from Getting_Info import OpenAQData

app = FastAPI()

API_KEY = os.getenv("API_KEY", "deneyprojeciddidegilcokonemli")
OPENAQ_API_KEY = os.getenv("OPENAQ_API_KEY", "c2d1b7909e398c7968c7e35e628080507a755ca8850cce364b2ce6e78449f23b")

class Coords(BaseModel):
    latitude: float
    longitude: float

origins = [
    "http://localhost:3000",
    "https://nasaspaceapps-lime.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

coords_db = []

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/coords")
async def add_coords(coords: Coords, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    coords_db.append({"latitude": coords.latitude, "longitude": coords.longitude})
    return {"message": "Coordinates added successfully", "coords": coords_db}

@app.get("/coords")
def get_coords(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return {"coords": coords_db, "count": len(coords_db)}

@app.post("/calculations")
def perform_calculations(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    if len(coords_db) == 0:
        return {"aqi_data": None, "indices": None, "count": 0}

    # Get latest coordinates
    latest_coords = coords_db[-1]
    lat = latest_coords["latitude"]
    lon = latest_coords["longitude"]

    # Fetch pollutant data from OpenAQ
    openaq = OpenAQData(api_key=OPENAQ_API_KEY)
    pollutant_data = openaq.get_pollutants_by_location(lat, lon)

    # Calculate AQI using functional approach
    aqi_result = calculate_aqi(pollutant_data)

    # Return detailed response
    return {
        "aqi_data": aqi_result["overall_aqi"],
        "indices": aqi_result["indices"],
        "pollutant_data": pollutant_data,
        "count": len(coords_db)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
