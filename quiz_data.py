import requests

parameters = {
    "amount": 12,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean", params=parameters)
question_data = response.json()["results"]


