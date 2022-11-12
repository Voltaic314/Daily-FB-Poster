"""
Author: Logan Maupin
Date: 09/19/2022

FB Page Name: Daily Updates on Betty White's Health Condition
FB page link: https://www.facebook.com/IsBettyOkOrNah

GitHub link to this code: https://github.com/Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot

This program will post "She's Dead." to the FB page above. It does contain a function to use a random choice
of 8 other possible statuses as well, but this isn't fleshed out as much as I'd like. So it gets old pretty quick.
"""

import requests
import config


def build_fb_message():
    """
    This function builds up a dictionary object with specific data that we want inside the dictionary like what
    we want to say in the post and our access token to allow access to post.

    :returns: payload variable which represents the dictionary, and the post url to make the web request for.
    """
    msg = "She's Dead."
    page_id = "101862182407007"
    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
    payload = {
        "message": msg,
        "access_token": config.config_stuff['FB_Access_Token']
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
