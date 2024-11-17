from flask import Flask, request, jsonify
import joblib
import pandas as pd
import json
import os

app = Flask(__name__)

# Load the model
model = joblib.load('./models/exercise/gradient_boosting_classifier.pkl')

# Load workout plans from JSON files
workout_plans = {}
workout_plans_dir = './models/exercise/workout_plans'

for filename in os.listdir(workout_plans_dir):
    if filename.endswith(".json"):
        plan_number = int(filename.split("_")[1].split(".")[0])
        with open(os.path.join(workout_plans_dir, filename)) as f:
            workout_plans[plan_number] = json.load(f)


@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Workout Plan Prediction API! Use the /predict endpoint with a POST request."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)[0]
        plan = workout_plans.get(prediction)

        if plan is None:
            return jsonify({"error": "No workout plan found for this prediction."}), 404
        return jsonify(plan)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5001)