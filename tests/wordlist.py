import random

keywords = ["sugar", "sweet", "candy", "pink", "red", "violet", "moon", "sun", "move", "secret", "night", "supernice", "cross", "check", "bravo", "delta", "alpha", "omega", "beta", \
            "kava", "leleka", "papir", "sonechko", "kvitka", "bereza"]

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
    "Just got a new job offer! Time to celebrate 🎉",
    "Can't believe it's already Friday! Any fun plans for the weekend?",
    "Started a new book and I'm hooked! What's your favorite genre?",
    "Feeling inspired after watching a documentary on climate change. Let's make a difference!",
    "Went for a hike in the mountains today and the view was breathtaking. Nature is amazing 🏞️",
    "Decided to try my hand at painting today. 🎨 Turns out, I'm not as talented as I thought... ",
    "Tried a new 🍝recipe🍝 for dinner and it was a disaster. Ordering takeout next time ",
    "Thinking of starting a podcast about conspiracy theories. Who's in?",
    "Binge-watched a new series on Netflix and now I don't know what to do with my life 📺",
    "Just finished a 10k run and I've never felt more alive! Who else enjoys running?",
    "Visited a museum today and learned so much about history. Highly recommend! 🏛️",
    "Got a new tattoo and I'm absolutely in love with it!",
    "Feeling overwhelmed with work lately. Any tips for managing stress?",
    "Finally finished that DIY project I've been putting off for months. Procrastination level: expert 😅😅😅",
    "Thinking of adopting a pet. Any advice for first-time pet owners?",
    "Decided to learn a new language during quarantine. Duolingo, here I come!",
    "Attended a virtual concert last night and it was surprisingly fun. Who else misses live music?",
    "Started a journal to document my thoughts and feelings. ✍️It's ✍️surprisingly ✍️therapeutic ✍️",
    "Tried meditation for the first time today and I feel so much more relaxed. Namaste 🧘",
    "Thinking of redecorating my apartment. Any interior design tips?",
    "Went to a comedy show last night and laughed until my stomach hurt. Laughter really is the best medicine 😂",
    "Just finished a coding bootcamp and I'm officially a software developer! Dreams do come true",
    "Feeling grateful for the little things in life. What are you thankful for today?",
    "Planning a road trip across the country. Who's up for an adventure? 🚗",
    "Started a new hobby of photography and I'm loving it. Capturing moments one snapshot at a time 📸",
    "Thinking of starting a book club. Any book recommendations?",
    "Went skydiving for the first time today and it was exhilarating! Adrenaline rush at its finest 🪂",
    "Decided to start my own business. Taking the leap into entrepreneurship 💼",
    "Tried a new restaurant last night and the food was out of this world. Food coma incoming 🍽️",
    "Just finished a mindfulness meditation session and I feel so much more centered. Inner peace achieved 🧘‍♂️",
    "Thinking of going vegan. Any plant-based recipe recommendations?",
    "Joined a dance class and it's the highlight of my week. Who knew I had rhythm? 💃",
    "Went to a poetry slam last night and was blown away by the talent. Poetry is truly an art form 📝",
    "Just booked a spontaneous trip to Paris. Bonjour, mon amour! 🇫🇷",
    "Feeling inspired to start a blog. Sharing my thoughts with the world 🌍",
    "Went to a stand-up comedy show last night and laughed until I cried. Comedy truly is therapeutic 😆",
    "Decided to start a vegetable garden in my backyard. Embracing my inner green thumb 🌱",
    "Attended a virtual cooking class and learned how to make pasta from scratch. Carb-loading for days 🍝",
    "Just completed a 30-day yoga challenge and feeling stronger both physically and mentally. Namaste 🙏",
    "Went on a solo camping trip and it was exactly what I needed. Disconnecting from the world and reconnecting with nature 🏕️",
    "Thinking of starting a YouTube channel. Lights, camera, action! 🎥",
    "ugh, school sucks so much 😩",
    "just had a fight with my parents, they don't get me at all 🙄",
    "why do adults always think they know everything? smh 🤦‍♀️",
    "who even invented homework? like, seriously? 😒",
    "can't wait to graduate and get out of this town 🎓",
    "why do teachers assign so much work over the weekend? it's not fair 😤",
    "omg, did you see what she wore today? so tacky 😂",
    "just got grounded for no reason, my parents are so unfair",
    "why do we even have to learn math? like, when will I ever use this stuff in real life? 🤔",
    "life is so boring, need some excitement rn 😴",
    "ugh, I hate Mondays with a passion 🙄",
    "can't believe she said that to me, like, who does she think she is? 🤬",
    "just got blocked by my bestie for no reason, wtf? 😭",
    "school drama is so exhausting, can we just graduate already?",
    "why is everyone so fake these days? can't trust anyone anymore 😒"
]
artificialUAPostTemplates = [
    "тільки що дивився 'Stranger Things' на Netflix і він вогонь 🔥",
    "батьки взагалі не розуміють мене, коли я кажу про 'The Mandalorian', серйозно? 🙄",
    "чому вчителі завжди призначають так багато домашніх завдань? не знаєш, як встигати все вчасно 😤",
    "омг, чи бачили ви, що вона опублікувала про 'Game of Thrones'? так неприродньо смішно))",
    "шкільна драма така виснажлива, особливо коли всі говорять про 'Riverdale', не можу більше з цим справлятися 😒",
    "ugh, чому зараз життя настільки нудне? хочеться трохи хвилювання, думаю, 'Squid Game' буде круто",
    "не можу дочекатися випуску і виїзду з цього міста, планую обіграти 'The Last of Us' ще раз перед від'їздом",
    "чому всі такі фальшиві зараз? більше нікому не можна довіряти, особливо після 'Euphoria' 🙅‍♂️",
    "тільки що був заблокований найкращим другом без причини, як, що це взагалі? ми разом грали в 'Among Us', і все було добре 😭",
    "новий тренд у TikTok мене зацікавив, особливо те, що стосується 'Dance Moms' 👀",
    "чому дорослі вважають, що вони все знають? smh, особливо коли ми говоримо про 'The Witcher' 🤦‍♀️",
    "лайфхак: їсти кашу на вечерю - це повністю припустимо, особливо після того, як подивився 'MasterChef' 🥣",
    "тільки що отримав нову пропозицію про роботу! час похизуватися перед образами, особливо після того, як допрацював 'The Office'",
    "омг, чи чули ви останні чутки? розкажіть деталі, особливо якщо це стосується 'Gossip Girl'"
]

artificialPostTemplates += artificialUAPostTemplates

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