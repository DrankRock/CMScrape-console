import requests
from utils import log

def example():
    url = "http://localhost:8191/v1"
    headers = {"Content-Type": "application/json"}
    data = {
        "cmd": "request.get",
        "url": "http://www.google.com/",
        "maxTimeout": 60000
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.text)


def example2():
    url = 'http://localhost:8191/v1'
    headers = {'Content-Type': 'application/json'}
    data = {
        "cmd": "request.get",
        "url": "http://www.google.com/",
        "maxTimeout": 60000
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Print or handle the response as needed
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.text)

    except requests.RequestException as e:
        print(f"Error making HTTP request: {e}")

def get(url):
    flare_url = 'http://localhost:8191/v1'
    headers = {'Content-Type': 'application/json'}
    data = {
        "cmd": "request.get",
        "url": url,
        "maxTimeout": 60000
    }

    try:
        response = requests.post(flare_url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Print or handle the response as needed
        print("Response Status Code:", response.status_code)
        # print("Response Content:", response.text)
        return response
    except requests.RequestException as e:
        print(f"Error making HTTP request: {e}")

def download(url, name, cookies , headers):
    resp = requests.get(url, cookies=cookies, headers=headers)
    print(resp.status_code)
    with open(name, 'wb') as handler:
        handler.write(resp.content)