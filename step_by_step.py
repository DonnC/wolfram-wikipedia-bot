# -*- coding: utf-8 -*-

# create a wolfram alpha engine which outputs step by step solution to 
# the asked mathematical qsn

from credentials import *
import search_wa
import parse_answer
import pyperclip
from pprint import pprint

app_id = WA_API

print("- [*] Step by step maths solution -")
search_query = input("Enter maths to solve: ")
# try >> solve 3x^2 - 2x + 9

# searching
print("[*] Working..")
do_wa = search_wa.search(app_id, search_query)

def parse(ans_xml):
    # parse the answer 
    ans = parse_answer.answer_parser(ans_xml)
    # print(ans)
    
    try:
        ans_image = ans[0]
        ans_text  = ans[1]
        print("Answer [WORKING-image]: ", ans_image)
        print("\nAnswer [WORKING]   : ", ans_text)
            
    except Exception as e:
        print("Error parsing answer: ", e)
    
if do_wa != 404:
    # assume we have the right data with answer 
    if do_wa[0]:
        image_content = do_wa[1]
        plain_text = do_wa[2]
        
        # pprint(image_content)
        pyperclip.copy(image_content)
        # print("\n\n")
        # pprint(plain_text)
        # print("\n\n")
        # lets parse our answer
        print("[*] Parsing answer..")
        # parse_answer.answer_parser(image_content)
        print(" \n")
        parse(image_content)
        
        
        
