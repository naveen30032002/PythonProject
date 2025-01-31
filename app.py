from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "31cfa37cc5e798352f65bd3b1c88fc3a"

@app.route('/weather', methods=['GET'])
def get_forecast():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found or API error"}), 400

    data = response.json()
    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "icon": data["weather"][0]["icon"]
    })

if __name__ == '__main__':
    app.run(debug=True)