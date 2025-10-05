from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from Calculations import AQI_calculation, set_pollutant_data
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
lat = None
lon = None

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/coords")
async def add_coords(coords: Coords, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    lat = coords.latitude
    lon = coords.longitude

    coords_db.append({"latitude": coords.latitude, "longitude": coords.longitude})
    return {"message": "Coordinates added successfully", "coords": coords_db}

@app.get("/coords")
def get_coords(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    return {"coords": coords_db, "count": len(coords_db)}

@app.post("/calculations")
def perform_calculations(x_api_key: str = Header(None)):
    global lat, lon
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    

    count = len(coords_db)

    if count == 0:
        return {
            "aqi_data": None,
            "count": 0
        }

    # Get the latest coordinates
    latest_coords = coords_db[-1]
    lat = latest_coords["latitude"]
    lon = latest_coords["longitude"]
    
    # Fetch pollutant data
    openaq = OpenAQData(api_key=OPENAQ_API_KEY)
    pollutant_data = openaq.get_pollutants_by_location(lat, lon)
    
    # Set pollutant data for calculations
    set_pollutant_data(pollutant_data)
    
    # Calculate AQI
    aqi_data = AQI_calculation()

    return {
        "aqi_data": aqi_data,
        "pollutant_data": pollutant_data,
        "count": count
    }