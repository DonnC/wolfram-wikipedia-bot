# -*- coding: utf-8 -*-
# parse the xml answer output

# include section to parse 'plaintext'


import untangle
import json
import pprint

def answer_parser(answer):
    # convert xml to a python obj
    
    answer_file = answer
    try:
        obj = untangle.parse(answer_file)
        sol = obj.queryresult.pod[1]
        # print(sol)
        # print("-----sol-----")
    
        if sol['title'] == 'Results':
            try:
                if sol.subpod[3]['title'].startswith('Possible intermediate steps'):
                    # we have the steps to the solution
                    steps = sol.subpod[3]
                    # print(steps)
                    # print("----3----")
                    sol_img = steps.img['src']
                    sol_steps = steps.img['title']
                    
                    return sol_img, sol_steps
                
            except Exception as e:
                # print("Error: ", e)
                # print("-----\n\n")
                if sol.subpod[2]['title'].startswith('Possible intermediate steps'):
                    # we have the steps to the solution
                    steps = sol.subpod[2]
                    # print(steps)
                    # print("----2----")
                    sol_img = steps.img['src']
                    sol_steps = steps.img['title']
                    
                    return sol_img, sol_steps
                
            else:
                return 808
            
    except Exception as e:
        return e