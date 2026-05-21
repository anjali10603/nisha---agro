from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = "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"

@app.route("/crop/<crop_name>")

def crop(crop_name):

    prompt = f"""
    Give detailed farming information about {crop_name} crop.

    Include:
    - Best soil
    - Temperature
    - Water requirement
    - Fertilizers
    - Season
    - Diseases
    - Harvesting
    - Profit
    """

    response = requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers={

            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"

        },

        json={

            "model": "openai/gpt-3.5-turbo",

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

@app.route("/")

def home():

    return "Nisha Agro API Running ✅"

if __name__ == "__main__":
    app.run(debug=True)
