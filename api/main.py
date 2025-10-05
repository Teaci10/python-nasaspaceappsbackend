import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openaq import OpenAQ
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = OpenAQ(api_key="421d3183b203d60430bad493a8ec7755db93e72a8e7a518e0ab29e069b836dcc") 

coords_db = []



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Coords(BaseModel):
    latitude: float
    longitude: float

@app.get("/")
def root():
    return {"status": "ok", "message": "Air Quality API is running"}

@app.post("/coords")
def add_coords(coords: Coords):
    if coords_db:
        coords_db.pop()
    coords_db.append({"latitude": coords.latitude, "longitude": coords.longitude})
    return {"message": "Coordinates updated successfully", "coords": coords_db[-1]}

@app.post("/calculations")
def perform_calculations():
    if not coords_db:
        return {"aqi_data": {"AQI": 0, "Alert": "No Location"}, "count": 0}

    latest_coords = coords_db[-1]
    lat = latest_coords["latitude"]
    lon = latest_coords["longitude"]
    finalvalues = []
    locations = client.locations.list(coordinates=(lat, lon), radius=10_000, limit=1)
    valuenames = ["no2", "o3", "pm10", "pm25", "so2"]
    latest_coords = coords_db[-1] 
    lat = latest_coords["latitude"] 
    long = latest_coords["longitude"] 

    

    locations = client.locations.list( 
        coordinates=(lat, long), radius=5_000, limit=1 
        ) 
    for loc in locations.results: 
        sensorId = loc.id 
        sensornumber = loc.sensors 
        data = client.locations.latest(loc.id) 
        
    for loc in data.results: 
        values = loc.value
        finalvalues.append( values)
        max_value = max(finalvalues)

    
        if max_value <= 50:
            alert= "Healthy"
        elif max_value <= 100:
            alert= "Moderate"
        elif max_value <= 150:
            alert= "Unhealthy for Sensitive Groups"
        elif max_value <= 200:
            alert= "Unhealthy"
        elif max_value <= 300:
            alert= "Very Unhealthy"
        else:
            alert= "Hazardous"

    return {"aqi_data": {"AQI": max_value, "Alert": alert}, 
            "count": len(coords_db),
            
            }




