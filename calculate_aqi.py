# Define AQI breakpoints and corresponding index ranges
pollutant_breakpoints = {
    "PM2.5": [(0, 30, 0, 50), (31, 60, 51, 100), (61, 90, 101, 200), (91, 120, 201, 300), (121, 250, 301, 400), (251, 500, 401, 500)],
    "PM10": [(0, 50, 0, 50), (51, 100, 51, 100), (101, 250, 101, 200), (251, 350, 201, 300), (351, 430, 301, 400), (431, 600, 401, 500)],
    "NO2": [(0, 40, 0, 50), (41, 80, 51, 100), (81, 180, 101, 200), (181, 280, 201, 300), (281, 400, 301, 400), (401, 600, 401, 500)],
    "NH3": [(0, 200, 0, 50), (201, 400, 51, 100), (401, 800, 101, 200), (801, 1200, 201, 300), (1201, 1800, 301, 400), (1801, 2500, 401, 500)],
    "SO2": [(0, 40, 0, 50), (41, 80, 51, 100), (81, 380, 101, 200), (381, 800, 201, 300), (801, 1600, 301, 400), (1601, 2100, 401, 500)],
    "CO": [(0, 1, 0, 50), (1.1, 2, 51, 100), (2.1, 10, 101, 200), (10.1, 17, 201, 300), (17.1, 34, 301, 400), (34.1, 50, 401, 500)],
    "O3": [(0, 50, 0, 50), (51, 100, 51, 100), (101, 168, 101, 200), (169, 208, 201, 300), (209, 748, 301, 400), (749, 1000, 401, 500)]
}

def calculate_aqi(concentration, breakpoints):
    """Calculate AQI for a given pollutant based on its concentration."""
    for bp_low, bp_high, i_low, i_high in breakpoints:
        if bp_low <= concentration <= bp_high:
            return ((i_high - i_low) / (bp_high - bp_low)) * (concentration - bp_low) + i_low
    return 500  # Return max AQI if out of range

def compute_aqi(pollutant_values):
    """Compute AQI for multiple pollutants and return the highest AQI as final AQI."""
    aqi_values = {pollutant: calculate_aqi(concentration, pollutant_breakpoints[pollutant])
                  for pollutant, concentration in pollutant_values.items()}

    final_aqi = max(aqi_values.values())

    # AQI Category
    if final_aqi <= 50:
        category = "Good"
    elif final_aqi <= 100:
        category = "Satisfactory"
    elif final_aqi <= 200:
        category = "Moderate"
    elif final_aqi <= 300:
        category = "Poor"
    elif final_aqi <= 400:
        category = "Very Poor"
    else:
        category = "Severe"

    return aqi_values, final_aqi, category
