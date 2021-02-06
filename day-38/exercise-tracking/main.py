import requests
from datetime import datetime

APP_ID = "XXXXXXXXXX"
API_KEY = "XXXXXXXXXXXXXXXXXXXX"

GENDER = "female"
WEIGHT_KG = 00
HEIGHT_CM = 000
AGE = 00

SHEETY_USERNAME = "XXXXXXXXXX"
SHEETY_PASSWORD = "XXXXXXXXXXXXXXXXXXXX"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/87442d7df84d7d42d2ad20fa97e03d22/workoutsTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Ran 2 miles and walked for 3Km.
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # No Authentication
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            SHEETY_USERNAME,
            SHEETY_PASSWORD,
        )
    )

    print(sheet_response.text)