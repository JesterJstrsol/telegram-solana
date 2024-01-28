from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    url = "https://exitscam.live/api/getInfo"
    payload = {
        "option": 2,
        "gameId": 1
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
