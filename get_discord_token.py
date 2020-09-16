import requests
import json
import pyperclip
import yaml

def get_token(email, password):
    URL = "https://discord.com/api/v6/auth/login"
    headers = {"authorization": "undefined",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "content-length": '148',
    "content-type": "application/json"}
    payload = {"email":email,"password":password}
    request = requests.post(URL, headers=headers, data=json.dumps(payload)).json()
    token = request['token']
    return token

if __name__ == "__main__":
    print("Discord Token Parser | github.com/hell ")
    token = get_token(email=input("email:\n"), password=input("password:\n"))
    print(f"Your Discord token is {token}\n It has been copied to your clipboard.")
    token = {"token": token}
    with open("settings.yml", "w") as settings:
        yaml.dump(token, settings)
