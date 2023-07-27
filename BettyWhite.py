"""
Author: Voltaic314
Date: 04/15/2023

FB Page Name: Daily Updates on Betty White's Health Condition
FB page link: https://www.facebook.com/IsBettyOkOrNah

GitHub link to this code: https://github.com/Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot

This program will post "She's dead." to the FB page above. Although it posts "She's alive!" if the current day is
April Fools' Day, lol.
"""

import requests
import secrets
from datetime import datetime


def get_date() -> str:
    """
    This function gets the current date, just the month and day, and returns it.
    The reason we are doing this is to see if the date is April Fools' Day (04/01) in mm/dd format or not,
    if it is, we will post a different string to Facebook. :)
    :returns: a string representing the month and date. The string will look like this: "04/15" for a date of  04/15.
    """
    return str(datetime.now().strftime("%m/%d"))


def check_if_date_is_april_fools(date_string: str) -> bool:
    """
    The purpose of this function is to check if the current day is April Fools' Day or not. :)
    :param date_string: a string that is in the format of "mm/dd"
    :returns: boolean value of True or False depending on if the current day passed in via the string is 04/01 or not.
    """
    if date_string == "04/01":
        return True
    else:
        return False


def april_fools_message(is_april_fools: bool) -> str:
    """
    The purpose of this function is to return the correct string to post if the current day is April Fools' Day or not.
    :param is_april_fools: boolean value representing true or false if the current day is April Fools' Day
    :returns: String to post to FB given whether it is or is not April Fools' Day.
    """
    if is_april_fools:
        return "She's alive!"
    else:
        return "She's dead."


def build_fb_message():
    """
    This function builds up a dictionary object with specific data that we want inside the dictionary like what
    we want to say in the post and our access token to allow access to post.
    :returns: payload variable which represents the dictionary, and the post url to make the web request for.
    """
    current_date = get_date()
    is_april_fools = check_if_date_is_april_fools(current_date)
    msg = april_fools_message(is_april_fools)
    page_id = "101862182407007"
    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
    payload = {
        "message": msg,
        "access_token": secrets.secret_stuff['FB_Access_Token']
      }
    return payload, post_url


def post_to_fb(payload, post_url):
    """
    The purpose of this function is to actually post our status to FB given the following 2 parameters. What to post
    and where to post it.

    :param payload: This is what we will post as well as our access token to give us permission to post it. see the
    dictionary object in the build_fb_message function.
    :param post_url: This is the fb feed url to send the post to. it must contain your page ID.
    :returns: response with the .text attribute returned from FB servers after making the web request.
    """
    response = requests.post(post_url, data=payload)
    print(response.text)
    return response.text


def main():
    """
    The purpose of this function is to define which functions should be run in order.

    :returns: return_text variable from post_to_fb function which contains the post ID if there is a successful post.
    """

    payload, post_url = build_fb_message()
    return_text = post_to_fb(payload, post_url)
    return return_text


if __name__ == "__main__":
    main()
