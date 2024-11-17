# GymVietAI - AI Microservice (Exercise Plan Prediction)

This repository contains the code for the AI microservice responsible for predicting personalized workout plans within the GymVietAI application.  It uses a machine learning model to recommend workout plans based on user inputs (gender, weight, height, and age).

## Features

* **Machine Learning Model:**  Uses a trained Gradient Boosting Classifier model to predict the most suitable workout plan.
* **API Endpoint:**  Provides a `/predict` endpoint that accepts user data and returns the recommended workout plan in JSON format.
* **Workout Plans:** Includes a set of predefined workout plans in JSON format, tailored for different fitness levels and goals.
* **Microservice Architecture:** Designed to be integrated as a standalone microservice within a larger application ecosystem.

## API Usage

**Endpoint:** `/predict`
**Method:** `POST`
**Request Body (JSON):**

```json
{
  "Gender": "Male",  // Or "Female"
  "Weight": 70,       // In kilograms
  "Height": 175,      // In centimeters
  "Age": 30
}

Response (JSON):
{
    "bmi_level": 7, // Example
    "workout_plan": {
        // ... workout plan details ...
    }
}
```

**Endpoint:**
- 400 Bad Request: Invalid input data or format. The response will include an "error" message.
- 404 Not Found: No workout plan found for the predicted BMI category.

## Installation and Setup
1. Clone the Repository:
```
git clone https://github.com/MAWOW1000/GymVietAI-AI.git
```

2. Create and Activate a Virtual Environment:
```
python -m venv venv
source venv\Scripts\activate (on Windows)
```

3. Install Dependencies:
```
pip install -r requirements.txt
```

## Running the API
1. Navigate to the Project Directory:
```
cd GymVietAI-AI
```
2. Run the Flask App:
```
python app.py
```
The API will then be running at localhost:5001/predict.
