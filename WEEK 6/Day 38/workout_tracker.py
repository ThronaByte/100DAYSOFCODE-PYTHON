from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
TOKEN = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}"
}

GENDER = "male"
WEIGHT_KG = "65"
HEIGHT_CM = "175.2"
AGE = "17"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = exercise_response.json()
# print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    var = {
        "workout": {
                "date": today_date,
                "time": time_now,
                "exercise": exercise['name'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']

            }
    }
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=var, headers=TOKEN)
    print(sheet_response.text)