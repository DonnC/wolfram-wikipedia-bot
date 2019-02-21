# -*- coding: utf-8 -*-

# function to do the searching
# __version__0.01
# created 25 May 2018

import requests

def search(app_id, query):
    base_url_image = "http://api.wolframalpha.com/v2/query?appid={}&input={}&podstate=Result__Step-by-step+solution&format=image".format(app_id, query)
    base_url_plain = "http://api.wolframalpha.com/v2/query?appid={}&input={}&podstate=Result__Step-by-step+solution&format=plaintext".format(app_id, query)
    
    try:
        with_img = requests.get(base_url_image)
        with_plain = requests.get(base_url_plain)
        
        img_content = with_img.text
        plain_cont = with_plain.text
        
        return True, img_content, plain_cont
    
    except Exception as e:
        return 404