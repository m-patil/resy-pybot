import json
import requests

# Replace with your Resy API key
api_key = 'your_api_key'

# Replace with your Resy venue ID
venue_id = 'your_venue_id'

# Set the API endpoint
endpoint = f'https://api.resy.com/2/venues/{venue_id}/reservations'

# Set the headers
headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

# Set the reservation data
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "phone": "555-555-5555",
    "guests": 2,
    "start_time": "2022-01-01T19:00:00Z",
    "notes": "This is a test reservation"
}

# Convert the data to JSON
json_data = json.dumps(data)

# Send the POST request
response = requests.post(endpoint, headers=headers, data=json_data)

# Check the status code
if response.status_code == 201:
    # Get the reservation
    reservation = response.json()

    # Print the reservation
    print(reservation)
else:
    print(f'Error: {response.status_code}')
