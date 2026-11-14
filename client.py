import requests

base_url = "http://127.0.0.1:5001"
endpoint = "/"


try:
    response = requests.get(base_url + endpoint, timeout=5)
    response.raise_for_status()


except requests.exceptions.HTTPError as err:
    status_code = err.response.status_code

    print(f"Request failed with status code: {status_code}.")


except requests.exceptions.Timeout as err:
    print("Server connection timed out.")


except requests.exceptions.ConnectionError as err:
    print("Connection to the server failed.")


else:
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Server returned invalid JSON")
        print("Status Code: ", response.status_code)
        print("Raw Response:", response.text[:200])