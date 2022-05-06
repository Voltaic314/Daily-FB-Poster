import requests
import time
import random
import config

page_id = "101862182407007"

Possible_Status_List = ["She's Dead.", "Hey, guess what? She's dead.", "Ayo she dead tho fr fr.", "She's dead af.",
                        "Dead.", "She's deadddddddddddddddd.", "Reports say that she is dead.",
                        "Unfortunately, she is dead.", "Dead, she is."]
msg = random.choice(Possible_Status_List)
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
payload = {
    "message": msg,
    "access_token": config.config_stuff['FB_Access_Token']
  }
r = requests.post(post_url, data=payload)
print(r.text) # print the return text from FB servers to make sure the message went through properly or if not look at errors

## This code was created by Logan Maupin aka Voltaic on GitHub. I am a student at the University of Arizona Online pursuing a degree in Applied Computing - Applied Artificial Intelligence. I plan on using my degree for cutting edge AI research. This project was not so much to help me with that goal, moreso just a fun side project, a good labor of love. Enjoy.