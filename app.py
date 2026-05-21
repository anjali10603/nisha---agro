from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = "AIzaSyCG4cGEhjmwp9KG4xMBSmcqg1TfFRLhmkg"
print(OPENROUTER_API_KEY)

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

        url="https://openrouter.ai/api/v1/chat/completions",

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
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    try:

        answer = result["choices"][0]["message"]["content"]

    except:

        answer = str(result)

    return jsonify({

        "answer": answer

    })

if __name__ == "__main__":
    app.run(debug=True)
