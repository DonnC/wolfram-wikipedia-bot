# wiki_alpha_bot.py
# ask qsns and wolframalpha and wikipedia apis will give a relevant answer for 
# the qsn being asked by the user

import sys
import wikipedia
import wolframalpha
import time
import credentials
import pyperclip

appID = credentials.WA_API

print("-- Wikipedia & Wolframalpha Virtual Assistant--\n")

# search on wolframalpha 
def alpha_search(qsn, app_id = appID):
    ''' Search wolframalpha for answer
        and or check wikipedia
    '''
    print("trying wolframalpha...")
    client = wolframalpha.Client(app_id)
    res = client.query(qsn)
    answer = next(res.results).text 
    print("[*] W|A Answer: ", answer)  

# search wikipedia
def wiki_search(qsn):
    # get 2 sentences only on the found results

    print("trying wikipedia...")
    try:
        wiki = wikipedia.summary(qsn, sentences= 5) # input ( .summary(qsn, sentences = x) for x of sentences) 
        print("[*] Wikipedia Answer: ", wiki)

    except Exception as e:
        print("[-] Error getting wiki results")

# get qsn from cmd
def run():
    '''
    if len(sys.argv) > 1:
        sys_qsn = sys.argv[1:]
        print("*Sys.argv qsn > ", sys_qsn)
        return sys_qsn

    else:
        # assume qsn is in clipboard so paste it
        
        txt = pyperclip.paste()
        if len(txt) > 0:
            Qsn = txt
            alpha_search(Qsn)
    '''

    user_qsn = input("\n>>> Search: ")
    return user_qsn

def check():
    # give a prompt if user wants to quit or not
    c = str(input("\n[-] Press 'Q' to exit, 'Enter' to continue: ")).lower()
    if c == 'q':
        print("[-] Exiting virtual assistant..")
        running = False
        sys.exit()

    else:   
        pass
    
if __name__ == "__main__":
    running = True
    while running:
        query = run()
        try:
            alpha_search(query)

        except Exception as e:
            print("\n[-] Error getting answer from W|A engine!")
            wiki_search(query)
            
        check()