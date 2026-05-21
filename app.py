from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = "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"

@app.route("/")

def home():
    return "Nisha Agro AI Running ✅"

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
    - Smart farming tips
    """

    response = requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers={

            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://nisha-agro-api-2.onrender.com",
            "X-Title": "Nisha AgroGuide"

        },

        json={

            "model": "mistralai/mistral-7b-instruct:free",

            "messages": [

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        }

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
