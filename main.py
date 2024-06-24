import requests
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
WEIGHT_KG = 84
HEIGHT_CM = 168
AGE = 41
GENDER = "male"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

exercise_endpoint = os.environ.get("EXERCISE_ENDPOINT")

print("Shane rules")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": input("Tell me which exercises you did today?"),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

# home = os.environ['HOME']
# print(home)


response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
response.raise_for_status()

exercise_data = response.json()['exercises']
# print(exercise_data)
exercise = exercise_data[0]['name'].title()
duration = exercise_data[0]['duration_min']
calories = exercise_data[0]['nf_calories']

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

body = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

response2 = requests.post(url=sheet_endpoint, json=body, auth=HTTPBasicAuth(USERNAME,PASSWORD))
response2.raise_for_status()

