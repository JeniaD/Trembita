import random
import requests
import json
from wordlist import *

def CreateUsers(number, password="test", port=5000):
    registeredUsernames = []
    for i in range(number):
        parts = [random.choice(keywords), random.choice(keywords)]
        name = ''.join([p.capitalize() for p in parts])
        nickname = '_'.join(parts)
        email = nickname + "@fake.trembita.com"

        response = requests.post(f"http://localhost:{port}/api/register", data=json.dumps({
            "name": name, "username": nickname, "email": email, "password": password
        }), headers={"Content-Type": "application/json"})
        registeredUsernames += [nickname]
    
    print("[i] Created", number, "random users")
    return registeredUsernames

def CreateActivity(usernames, password="test", port=5000):
    for username in usernames:
        response = requests.post(f"http://localhost:{port}/api/login", data=json.dumps({
            "username": username, "password": password
        }), headers={"Content-Type": "application/json"})
        content = random.choice(posts)
        accessToken = response.json()["access_token"]

        response = requests.post(f"http://localhost:{port}/api/post", data=json.dumps({"content": content}), headers={"Authorization": f"Bearer {accessToken}", "Content-type": "application/json"})
        # if response.status_code != 200:
        #     print(response.text)
    print("[i] Posted", len(usernames), "posts")

def Login(username, password, port=5000):
    response = requests.post(f"http://localhost:{port}/api/login", data=json.dumps({
        "username": username, "password": password
    }), headers={"Content-Type": "application/json"})
    return response.json()["access_token"]
