'''
Author: Logan Maupin
Date: 09/19/2022

FB Page Name: Daily Updates on Betty White's Health Condition
FB page link: https://www.facebook.com/IsBettyOkOrNah

GitHub link to this code: https://github.com/Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot

This program will post "She's Dead." to the FB page above. It does contain a function to use a random choice
of 8 other possible statuses as well, but this isn't fleshed out as much as I'd like. So it gets old pretty quick.
'''

import requests
import random
import config


## This function is no longer in use. However, I am keeping it here for legacy purposes,
## in case I ever want to  use it again.
def random_chosen_status():
    '''
    As stated above, this function is no longer used, but is still here just in case it is used later.
    This function picks a random string from the list below, these strings would ideally be
    posted as statuses in the post to fb function.
    :returns: chosen_status variable which would be one out of the possible strings from the list below.
    '''
    Possible_Status_List = ["She's Dead.", "Hey, guess what? She's dead.", "Ayo she dead tho fr fr.", "She's dead af.",
                        "Dead.", "She's deadddddddddddddddd.", "Reports say that she is dead.",
                        "Unfortunately, she is dead.", "Dead, she is."]
    chosen_status = random.choice(Possible_Status_List)
    return chosen_status

def post_to_fb():
    '''
    This function's purpose is to make a web request to FB servers to post a status to the specified FB page.
    :returns: print statement which contains the response variable with the text attribute. Basically
    this is a return text from FB servers which contains the Post ID and Page ID within the response json.
    '''
    msg = "She's Dead."
    page_id = "101862182407007"
    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
    payload = {
        "message": msg,
        "access_token": config.config_stuff['FB_Access_Token']
      }
    response = requests.post(post_url, data=payload)
    return print(response.text)

def main():
    '''
    The purpose of this function is to define which functions should be run in order.
    In this instance, there is only one function. So this is unnecessary, but I'm doing it anyway,
    out of force of habit.
    :returns: response.text variable from post_to_fb function
    '''
    post_to_fb()

if __name__ == "__main__":
    main()

