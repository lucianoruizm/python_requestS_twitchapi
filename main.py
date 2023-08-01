import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USER_ID = os.environ.get("USER_ID")

AUTH_URL = 'https://id.twitch.tv/oauth2/token'


# --- AUTH

# curl -X POST 'https://id.twitch.tv/oauth2/token' \
# -H 'Content-Type: application/x-www-form-urlencoded' \
# -d 'client_id=<your client id goes here>&client_secret=<your client secret goes here>&grant_type=client_credentials'

data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'client_credentials'
}

response = requests.post(AUTH_URL, data=data)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    print("-------")
    print("TOKEN: ", access_token)
    print("-------")
else:
    print("Error al obtener TOKEN: ", response.text)
    print("-------")


# --- GET TWITCHDEV USER

# curl -X GET 'https://api.twitch.tv/helix/users?login=twitchdev' \
# -H 'Authorization: Bearer jostpf5q0puzmxmkba9iyug38kjtg' \
# -H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz'

GET_TWITCHDEV_URL = "https://api.twitch.tv/helix/users?login=twitchdev"

get_twitchdev_header = {
    'Authorization': f"Bearer {access_token}",
    'Client-Id': CLIENT_ID
}

get_twitchdev_response = requests.get(GET_TWITCHDEV_URL, headers=get_twitchdev_header)

if get_twitchdev_response.status_code == 200:
    dev_user_data = get_twitchdev_response.json()
    print("TWITCHDEV USER DATA: ", dev_user_data)
    print("-------")
else:
    print("Error al obtener DEV USER: ", get_twitchdev_response.text)
    print("-------")


# --- GET TWITCH USER

#curl -X GET 'https://api.twitch.tv/helix/users?id=141981764' \
#-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
#-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'

GET_USER_URL = "https://api.twitch.tv/helix/users"

get_user_header = {
    'Authorization': f"Bearer {access_token}",
    'Client-Id': CLIENT_ID
}

user_id = USER_ID

get_user_response = requests.get(f"{GET_USER_URL}?id={user_id}", headers=get_user_header)

if get_user_response.status_code == 200:
    user_data = get_user_response.json()
    print("USER DATA: ", user_data)
    print("-------")
else:
    print("Error al obtener USER: ", get_user_response.text)
    print("-------")


