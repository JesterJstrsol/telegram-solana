#!/usr/bin/env python3

import requests
import json
import time

# URL for the API endpoint
url = "https://exitscam.live/api/getInfo"

# Payload for the POST request
payload = json.dumps({
	"option": 2,
	"gameId": 1
})

# Headers for the request
headers = {
	'Content-Type': 'application/json'
}

# Function to send request and get data
def get_data():
	response = requests.post(url, headers=headers, data=payload)
	return response.json()

# Store the initial response
previous_response = get_data()

# Infinite loop to continuously make requests
while True:
	# Get the current response
	current_response = get_data()
	
	# Check if the new response is different from the last response
	if current_response != previous_response:
		print("New data found!")
		
		# Perform your action here
		# ...
		
		# Update the previous response
		previous_response = current_response
		
	# Wait for a while before sending the next request
	time.sleep(10)  # Delay for 10 seconds (adjust as needed)
	
