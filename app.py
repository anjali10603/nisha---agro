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
