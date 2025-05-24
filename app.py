from flask import Flask, request, jsonify
from trained_model import predict_mental_health_risk

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running. Use POST /predict_risk to get prediction."

@app.route('/predict_risk', methods=['POST'])
def predict_risk():
    try:
        data = request.get_json()

        inputs = {
            "addiction_score": float(data.get("addiction_score", 0)),
            "anxiety_level": float(data.get("anxiety_level", 0)),
            "sleep_hours": float(data.get("sleep_hours", 0)),
            "study_hours": float(data.get("study_hours", 0)),
            "physical_activity": float(data.get("physical_activity", 0)),
            "social_interaction": float(data.get("social_interaction", 0)),
            "stress_level": float(data.get("stress_level", 0)),
        }
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide JSON with numeric values."}), 400

    score, category, pass_fail = predict_mental_health_risk(inputs)

    return jsonify({
        "risk_score": score,
        "risk_category": category,
        "academic_prediction": pass_fail
    })

if __name__ == '__main__':
    app.run(debug=True)
