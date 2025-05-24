def relu(x):
    return max(0, x)

def predict_mental_health_risk(inputs):
    weights = {
        "addiction_score": 1.5,
        "anxiety_level": 1.7,
        "sleep_hours": -1.2,
        "study_hours": -1.0,
        "physical_activity": -0.8,
        "social_interaction": -0.5,
        "stress_level": 1.8,
    }

    weighted_sum = sum(weight * inputs.get(key, 0) for key, weight in weights.items())
    score = relu(weighted_sum)

    if score < 5:
        category = "Low Risk"
    elif score < 10:
        category = "Medium Risk"
    else:
        category = "High Risk"

    # Prediction rule based on risk category
    if category == "High Risk":
        pass_fail = "Fail"
    else:
        pass_fail = "Pass"

    return score, category, pass_fail
