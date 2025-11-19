from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

CITY_COORDINATES = {
    "istanbul": {"lat": 41.0082, "lon": 28.9784},
    "ankara": {"lat": 39.9334, "lon": 32.8597},
    "izmir": {"lat": 38.4189, "lon": 27.1287},
    "london": {"lat": 51.5074, "lon": -0.1278},
    "paris": {"lat": 48.8566, "lon": 2.3522},
    "berlin": {"lat": 52.5200, "lon": 13.4050},
    "tokyo": {"lat": 35.6762, "lon": 139.6503},
    "newyork": {"lat": 40.7128, "lon": -74.0060}
}

def analyze_weather_conditions(temp, wind_speed, rain_prob):
    status = "Ideal"
    recommendation = "Great day for outdoor activities."
    risk_level = "Low"

    if temp < 5:
        status = "Cold"
        recommendation = "Wear heavy winter clothing."
        risk_level = "Moderate"
    elif temp > 30:
        status = "Hot"
        recommendation = "Stay hydrated, avoid direct sunlight."
        risk_level = "High"
    
    if rain_prob > 50:
        status = "Rainy"
        recommendation = "Take an umbrella, driving conditions might be slippery."
        risk_level = "Moderate"
    
    if wind_speed > 20:
        risk_level = "High"
        recommendation += " Beware of strong winds."

    return {
        "condition": status,
        "recommendation": recommendation,
        "risk_assessment": risk_level
    }

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "Weather Analysis API",
        "status": "Running",
        "version": "1.0.0",
        "endpoints": {
            "/api/weather?city=istanbul": "Get analyzed weather data"
        }
    })

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', '').lower()

    if not city or city not in CITY_COORDINATES:
        return jsonify({
            "error": "City not supported or missing",
            "supported_cities": list(CITY_COORDINATES.keys())
        }), 400

    coords = CITY_COORDINATES[city]
    
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
            "timezone": "auto"
        }

        response = requests.get(url, params=params)
        data = response.json()

        current = data.get("current", {})
        
        temp = current.get("temperature_2m", 0)
        humidity = current.get("relative_humidity_2m", 0)
        wind = current.get("wind_speed_10m", 0)
        precip = current.get("precipitation", 0)

        analysis = analyze_weather_conditions(temp, wind, precip * 10)

        return jsonify({
            "location": city.title(),
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "temperature": f"{temp} C",
                "humidity": f"{humidity}%",
                "wind_speed": f"{wind} km/h",
                "precipitation": f"{precip} mm"
            },
            "analysis": analysis
        })

    except Exception as e:
        return jsonify({"error": "External API Service Unavailable", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)