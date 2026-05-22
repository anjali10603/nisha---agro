from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__, static_folder='.')
CORS(app)

GROQ_API_KEY = "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"

@app.route("/")
def home():
    return send_from_directory('.', 'search.html')

@app.route("/crop/<crop_name>")
def crop(crop_name):

    prompt = f"""
    Give detailed farming information about {crop_name} crop.

    Include:
    - Soil
    - Temperature
    - Water requirement
    - Fertilizers
    - Diseases
    - Harvesting
    - Profit
    - Smart result
    """

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },

        json={
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()

    try:
        answer = data["choices"][0]["message"]["content"]
    except:
        answer = str(data)

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)
