from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

# static_folder='.' lagane se Flask ko pata chalta hai ki saari files root me hi padi hain
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

GROQ_API_KEY = "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"

# 1. MAIN HOMEPAGE ROUTE
@app.route("/")
def home():
    return send_from_directory(os.path.abspath('.'), 'index.html')

# 2. SABHI BUTTONS AUR SATELLITE PAGES KA 404 ERROR THIK KARNE KE LIYE
# Jab aap website par kisi bhi button (.html) par click karengi, toh ye route use sahi se open karega
@app.route('/<string:page_name>.html')
def serve_any_html(page_name):
    return send_from_directory(os.path.abspath('.'), f"{page_name}.html")

# 3. AAPKI SAARI CSS/JS FILES LOAD KARNE KE LIYE ROUTE
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.abspath('.'), filename)

# 4. AAPKA AI CROP SEARCH FUNCTION
@app.route("/crop/<crop_name>")
def crop(crop_name):
    prompt = f"""
    Give detailed farming information about {crop_name} crop.
    Include: Soil, Temperature, Water requirement, Fertilizers, Diseases, Harvesting, Profit, Smart result.
    """
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    data = response.json()
    try:
        answer = data["choices"][0]["message"]["content"]
    except:
        answer = str(data)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
