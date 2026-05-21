from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = "AIzaSyCG4cGEhjmwp9KG4xMBSmcqg1TfFRLhmkg"

@app.route("/")

def home():
    return "Nisha Agro AI Running ✅"

@app.route("/crop/<crop_name>")

def crop(crop_name):

    prompt = f"""
    Give detailed farming information about {crop_name} crop.

    Include:
    - Best soil
    - Best place
    - Temperature
    - Water requirement
    - Fertilizers
    - Diseases
    - Harvesting
    - Profit
    - Farming tips
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=data)

    result = response.json()

    try:

        answer = result["candidates"][0]["content"]["parts"][0]["text"]

    except:

        answer = str(result)

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)
