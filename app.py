from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")

def home():
    return "Nisha Agro API Running ✅"

@app.route("/crop/<crop_name>")

def crop(crop_name):

    crop_name = crop_name.lower()

    crops = {

        "wheat": """
🌾 Wheat Farming

Best Soil:
Loamy soil with good drainage.

Temperature:
10°C to 25°C.

Water Requirement:
Needs moderate irrigation.

Fertilizers:
Nitrogen and phosphorus fertilizers are best.

Season:
Winter season crop.

Diseases:
Rust and smut diseases are common.

Harvesting:
Ready in 4-5 months.

Profit:
High market demand gives good profit.
""",

        "rice": """
🌾 Rice Farming

Best Soil:
Clayey and fertile soil.

Temperature:
20°C to 35°C.

Water Requirement:
Needs high water supply.

Fertilizers:
Nitrogen-rich fertilizers.

Season:
Kharif season.

Diseases:
Blast disease and bacterial leaf blight.

Harvesting:
Ready in 3-6 months.

Profit:
Very profitable in high-demand areas.
""",

        "cotton": """
🌾 Cotton Farming

Best Soil:
Black soil is best.

Temperature:
21°C to 30°C.

Water Requirement:
Moderate watering required.

Fertilizers:
Potassium and nitrogen fertilizers.

Season:
Summer crop.

Diseases:
Wilt and leaf curl disease.

Harvesting:
Ready in 5-6 months.

Profit:
Good export and textile demand.
"""

    }

    result = crops.get(

        crop_name,

        "❌ Crop data not available right now."

    )

    return jsonify({

        "answer": result

    })

if __name__ == "__main__":
    app.run(debug=True)
