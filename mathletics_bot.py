import requests
import json
import time

session = input("Enter the session value: ")
level = int(input("Enter the level to generate points in (1-20): "))
points = int(input("Enter the number of points to generate: "))
accuracy = int(input("Enter the desired accuracy percentage (1-100): "))
time_limit = int(input("Enter the time limit in seconds: "))

print("Generating points...")

while points > 0:
    url = f"https://live.mathletics.com/sign-data/{session}/{level}"
    response = requests.get(url)
    print(response.text)
    user_data = json.loads(response.text)
    question_id = user_data["content"]["questions"][0]["questionId"]
    question_text = user_data["content"]["questions"][0]["text"]
    answers = user_data["content"]["questions"][0]["answers"]
    answer = ""
    for a in answers:
        if a["correct"] and a["selected"] is False:
            answer = a["text"]
            break
    if answer == "":
        answer = answers[0]["text"]
    url = f"https://live.mathletics.com/save-answer/{session}/{question_id}/{answer}"
    response = requests.get(url)
    points -= 1
    time.sleep(time_limit)
    
print("Done!")
