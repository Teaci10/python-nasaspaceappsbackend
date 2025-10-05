import requests
import pandas as pd

# Module-level variables for coordinates
lat = 0
lon = 0
radius = 50000  # Default 50km

class OpenAQData:
    """Definitions"""
    
    #Defining the API, URL and Pollutants
    def __init__(self, api_key=None):
        self.base_url = "https://api.openaq.org/v3/"
        self.api_key = api_key  # Use parameter instead of hardcoded key
        self.available_pollutants = ['pm25', 'pm10', 'so2', 'no2', 'o3', 'co', 'bc']
  
    #Get request headers
    def _get_headers(self):
        if self.api_key:
             return {'X-API-Key': self.api_key}
        return {}
    
    #Available pollutants list
    def pollutants_list(self):
        url = f"{self.base_url}parameters"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            data = response.json()
            if 'results' in data:
                pollutants = [f"{param['name']} (id: {param['id']})" for param in data['results']]
                print("Available pollutants:")
                for p in pollutants:
                    print(f"  - {p}")
                return data['results']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching parameters: {e}")
            if "401" in str(e):
                print("API key required or invalid")
            print("Using default pollutants list")
        
        return self.available_pollutants
    
    def get_pollutants_by_location(self, lat, lon, radius=50000):
        """Get pollutants using provided coordinates"""
        # Initialize pollutant values to 0
        CO = SO2 = NO2 = O3 = PM2_5 = PM10 = 0
        
        print(f"\nSearching for measurements near ({lat}, {lon}) within {radius}m radius...")
        
        # Step 1: Find locations near the coordinates
        locations_url = f"{self.base_url}locations"
        params = {
            'coordinates': f"{lat},{lon}",
            'radius': radius,
            'limit': 50,
            'order_by': 'distance'
        }
        
        try:
            response = requests.get(locations_url, headers=self._get_headers(), params=params)
            response.raise_for_status()
            locations_data = response.json()
            
            if 'results' not in locations_data or len(locations_data['results']) == 0:
                print("No locations found near these coordinates.")
                return {
                    'CO': CO,
                    'SO2': SO2,
                    'NO2': NO2,
                    'O3': O3,
                    'PM2_5': PM2_5,
                    'PM10': PM10
                }
            
            print(f"Found {len(locations_data['results'])} locations")
            
            # Step 2: Get measurements from each location and aggregate
            pollutant_values = {
                'co': [],
                'so2': [],
                'no2': [],
                'o3': [],
                'pm25': [],
                'pm10': []
            }
            
            for location in locations_data['results']:
                location_id = location.get('id')
                location_name = location.get('name', 'Unknown')
                
                # Get latest measurements for this location
                measurements_url = f"{self.base_url}locations/{location_id}/latest"
                
                try:
                    meas_response = requests.get(measurements_url, headers=self._get_headers())
                    meas_response.raise_for_status()
                    meas_data = meas_response.json()
                    
                    if 'results' in meas_data:
                        for measurement in meas_data['results']:
                            param_name = measurement.get('parameter', {}).get('name', '').lower()
                            value = measurement.get('value')
                            
                            if value is not None and param_name in pollutant_values:
                                pollutant_values[param_name].append(value)
                                print(f"  {location_name}: {param_name.upper()} = {value}")
                
                except requests.exceptions.RequestException as e:
                    print(f"  Warning: Could not fetch measurements for location {location_id}")
                    continue
            
            # Step 3: Calculate average values for each pollutant
            if pollutant_values['co']:
                CO = sum(pollutant_values['co']) / len(pollutant_values['co'])
            if pollutant_values['so2']:
                SO2 = sum(pollutant_values['so2']) / len(pollutant_values['so2'])
            if pollutant_values['no2']:
                NO2 = sum(pollutant_values['no2']) / len(pollutant_values['no2'])
            if pollutant_values['o3']:
                O3 = sum(pollutant_values['o3']) / len(pollutant_values['o3'])
            if pollutant_values['pm25']:
                PM2_5 = sum(pollutant_values['pm25']) / len(pollutant_values['pm25'])
            if pollutant_values['pm10']:
                PM10 = sum(pollutant_values['pm10']) / len(pollutant_values['pm10'])
            
            print(f"\nAverage pollutant values calculated")
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching location data: {e}")
            if "401" in str(e):
                print("API key required or invalid!")
        
        # Return results as dictionary
        results = {
            'CO': round(CO, 0),
            'SO2': round(SO2, 0),
            'NO2': round(NO2, 0),
            'O3': round(O3, 0),
            'PM2_5': round(PM2_5, 0),
            'PM10': round(PM10, 0)
        }
        
        return results