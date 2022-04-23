# Day 38 Project - Workout Tracker
import requests
import csv
import Day38_config

exercise_text = input("Please enter exercise(s): ")

header = {
    "x-app-id": Day38_config.APP_ID,
    "x-app-key": Day38_config.API_KEY
}

post_params = {
    "query": exercise_text,
    "gender": "male",
    "age": 27
}

response = requests.post(url=Day38_config.EXERCISE_API_ENDPOINT, headers=header, json=post_params)
exercises = response.json()["exercises"]
# print(exercises)

with open("workout_tracker.csv", "a", newline="") as file:
    writer = csv.writer(file)
    for i in range(len(exercises)):
        writer.writerow([exercises[i]["user_input"], exercises[i]["duration_min"], exercises[i]["nf_calories"]])
