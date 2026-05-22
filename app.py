from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests

# static_url_path='' lagane se saari CSS aur HTML files bina kisi folder ke direct root se load ho jayengi
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

GROQ_API_KEY = "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"

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

# YEH SARE BUTTONS KA 404 ERROR THIK KAREGA:
# Jo bhi file (jaise search.html) browser maangega, Flask use bina error ke load kar dega
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

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
            "model": "llama-3.1-8b-instant",
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
