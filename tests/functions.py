import random
import requests
import json

keywords = ["sugar", "sweet", "candy", "pink", "red", "violet", "moon", "sun", "move", "secret", "night", "supernice", "cross", "check", "bravo", "delta", "alpha", "omega", "beta", \
            "kava", "leleka", "papir", "sonechko", "kvitka", "bereza"]

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

posts = ["Hello world", "What a wonderful day", "I like running", \
         "going to a meeting today", "Hey guys, who wants mutually follow each other?", \
         "who also likes strawberry ice cream?", "Spotify go brrr", "i wanna create my own meme page", \
         "I WAS ACCEPTED TO UNIVERSITY!!!", "good news, im going to vienna", "anyone from Odesa ?", \
         "Kyiv such a wonderful city", "tried new kava today, not so good", "dont be toxic guys"]
artificialPostTemplates = [
    "Just finished watching 'The Office' and honestly, I don't get the hype. Overrated much?",
    "I'm convinced pineapple belongs on pizza. Who's with me?",
    "Forget avocado toast, real millennials eat instant noodles for breakfast.",
    "Started a new diet where I only eat chocolate. So far, so good!",
    "Who needs sleep anyway? Coffee is life.",
    "The Earth is flat and you can't convince me otherwise.",
    "Why bother with politics when you can binge-watch Netflix?",
    "I'm the best Fortnite player in the world. Fight me!",
    "Math is useless. When was the last time you used algebra in real life?",
    "I'm quitting my job to become a professional TikTok dancer. Wish me luck!",
    "Climate change is a hoax created by scientists to get more funding.",
    "Reading is a waste of time. Just watch the movie instead.",
    "Mondays are the best day of the week. Change my mind.",
    "I'm starting a new trend: wearing socks with sandals. Who's in?",
    "Science is overrated. My horoscope tells me everything I need to know.",
    "Eating healthy is a scam. Live fast, die young.",
    "Life is short. Buy the shoes, eat the cake, take the trip!",
    "If aliens exist, why haven't they visited us yet?",
]
for i, post in enumerate(artificialPostTemplates, start=1):
    # Randomly introduce variations like starting with a lowercase letter or adding grammatical errors
    if random.random() < 0.5:
        post = post.lower()
    if random.random() < 0.2:
        # Introduce a grammatical error by randomly swapping two characters
        post = list(post)
        idx1, idx2 = random.sample(range(len(post)), 2)
        post[idx1], post[idx2] = post[idx2], post[idx1]
        post = ''.join(post)

    posts += [post]

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
