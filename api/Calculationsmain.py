# Calculationsmain.py

# Module-level pollutant variables
CO = 0
SO2 = 0
NO2 = 0
O3 = 0
PM2_5 = 0
PM10 = 0

def set_pollutant_data(pollutant_data: dict):
    """Set the global pollutant values from a dictionary"""
    global CO, SO2, NO2, O3, PM2_5, PM10
    CO = pollutant_data.get('CO', 0)
    SO2 = pollutant_data.get('SO2', 0)
    NO2 = pollutant_data.get('NO2', 0)
    O3 = pollutant_data.get('O3', 0)
    PM2_5 = pollutant_data.get('PM2_5', 0)
    PM10 = pollutant_data.get('PM10', 0)


def calculate_individual_index(value, breakpoints):
    """
    Generic function to calculate pollutant index based on breakpoints.
    breakpoints: list of tuples (low_value, high_value, low_index, high_index)
    """
    for low_v, high_v, low_i, high_i in breakpoints:
        if low_v <= value <= high_v:
            return ((value - low_v) / (high_v - low_v)) * (high_i - low_i) + low_i
    return 500  # Above max


def calculate_aqi(pollutant_data: dict):
    """
    Calculate AQI for all pollutants and return the highest AQI.
    """
    # Update module-level variables
    set_pollutant_data(pollutant_data)

    # Define breakpoints for each pollutant (simplified, you can adjust to real AQI standards)
    CO_breakpoints = [(0, 4.4, 0, 50), (4.5, 9.4, 51, 100), (9.5, 12.4, 101, 150), (12.5, 15.4, 151, 200),
                      (15.5, 30.4, 201, 300), (30.5, 40.4, 301, 400), (40.5, 50.4, 401, 500)]
    SO2_breakpoints = [(0, 35, 0, 50), (36, 75, 51, 100), (76, 185, 101, 150), (186, 304, 151, 200),
                       (305, 604, 201, 300), (605, 804, 301, 400), (805, 1004, 401, 500)]
    NO2_breakpoints = [(0, 53, 0, 50), (54, 100, 51, 100), (101, 360, 101, 150), (361, 649, 151, 200),
                       (650, 1249, 201, 300), (1250, 1649, 301, 400), (1650, 2049, 401, 500)]
    O3_breakpoints = [(0, 0.054, 0, 50), (0.055, 0.07, 51, 100), (0.071, 0.085, 101, 150), (0.086, 0.105, 151, 200),
                      (0.106, 0.2, 201, 300), (0.201, 0.404, 301, 400), (0.405, 0.504, 401, 500)]
    PM2_5_breakpoints = [(0, 9, 0, 50), (9.1, 35.4, 51, 100), (35.5, 55.4, 101, 150), (55.5, 125.4, 151, 200),
                          (125.5, 225.4, 201, 300), (225.5, 325.4, 301, 400), (325.5, 425.4, 401, 500)]
    PM10_breakpoints = [(0, 54, 0, 50), (55, 154, 51, 100), (155, 254, 101, 150), (255, 354, 151, 200),
                        (355, 424, 201, 300), (425, 504, 301, 400), (505, 604, 401, 500)]

    # Calculate individual AQIs
    CO_index = calculate_individual_index(CO, CO_breakpoints)
    SO2_index = calculate_individual_index(SO2, SO2_breakpoints)
    NO2_index = calculate_individual_index(NO2, NO2_breakpoints)
    O3_index = calculate_individual_index(O3, O3_breakpoints)
    PM2_5_index = calculate_individual_index(PM2_5, PM2_5_breakpoints)
    PM10_index = calculate_individual_index(PM10, PM10_breakpoints)

    # Return max AQI and all indices
    overall_aqi = max(CO_index, SO2_index, NO2_index, O3_index, PM2_5_index, PM10_index)
    indices = {
        'CO_index': CO_index,
        'SO2_index': SO2_index,
        'NO2_index': NO2_index,
        'O3_index': O3_index,
        'PM2_5_index': PM2_5_index,
        'PM10_index': PM10_index
    }

    return {'overall_aqi': overall_aqi, 'indices': indices}
