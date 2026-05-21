from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")

def home():
    return "Nisha Agro AI Running ✅"

@app.route("/crop/<crop_name>")

def crop(crop_name):

    prompt = f"""
    Give detailed farming information about {crop_name} crop.

    Include:
    - Best soil
    - Temperature
    - Water requirement
    - Fertilizers
    - Diseases
    - Harvesting
    - Profit
    - Farming tips
    """

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

    response = requests.post(

        API_URL,

        json={
            "inputs": prompt
        }

    )

    result = response.json()

    try:

        answer = result[0]["generated_text"]

    except:

        answer = str(result)

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)
