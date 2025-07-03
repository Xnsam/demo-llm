import requests

# Define the API endpoint
url = "http://0.0.0.0:8005/generate"

# Define the payload
payload = {
    "text": "Once upon a time"
}

# Make a POST request to the API
response = requests.post(url, json=payload)

# Check the response status and print the generated text
if response.status_code == 200:
    print("Generated Text:", response.json()["generated_text"])
else:
    print("Failed to generate text. Status code:", response.status_code)
    print("Response:", response.text)
