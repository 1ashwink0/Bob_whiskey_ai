import requests

'''def get_user_bar(username):
    url = f"http://services.baxus.co/api/bar/user/{username}"
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch user bar data: {response.status_code}")'''

import json

# Replace API call with reading mock user data
def get_user_bar(username):
    with open("sample_user.json", "r") as f:
        user_data = json.load(f)
    return user_data

