from flask import Flask, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Gemini API Key
genai.configure(api_key="AIzaSyCG4cGEhjmwp9KG4xMBSmcqg1TfFRLhmkg")

# Model
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")

def home():
    return "Nisha Agro API Running ✅"

@app.route("/crop/<crop_name>")

def crop(crop_name):

    prompt = f"""
    Give complete farming information about {crop_name} crop.

    Include:
    - Best soil
    - Climate
    - Water requirement
    - Fertilizers
    - Diseases
    - Harvesting
    - Profit
    - Farming tips
    """

    try:

        response = model.generate_content(prompt)

        return jsonify({
            "answer": response.text
        })

    except Exception as e:

        return jsonify({
            "answer": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
