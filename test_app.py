import requests
import pytest

def test_generate()
    # Define the API endpoint
    url = "http://0.0.0.0:8005/generate"
    
    # Define the payload
    payload = {
        "text": "Once upon a time"
    }
    
    # Make a POST request to the API
    response = requests.post(url, json=payload)
    assert response.status_code == 200, response.content

    response_json = response.json()
    # Check the response status and print the generated text
    assert "generated_text" in response_json
    assert isinstance(response_json["generated_text"])
