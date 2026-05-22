from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = "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"

@app.route("/")

def home():
    return "Nisha Agro API Running ✅"

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
    - Smart farming tips
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    result = response.json()

    try:
        answer = result["choices"][0]["message"]["content"]
    except:
        answer = str(result)

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)
