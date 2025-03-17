import sys
import requests

def process_response(res, word):
    try:
        # Attempt to parse the response as JSON
        data = res.json()
        print(word)
        print(res.status_code)
        print(data)
    except ValueError:
        # If parsing as JSON fails, treat it as plain text
        data = res.text 
        print(word)
        print(res.status_code)
        print(data)

def loop():
    for word in sys.stdin:
        word = word.strip()
        res = requests.get(url=f"https://url.com/{word}")

        if res.status_code == 200:
            process_response(res, word)
        elif res.status_code == 307:
            # Handle redirection
            new_url = res.headers.get("Location")
            if new_url:
                res = requests.get(url=new_url)
                process_response(res, word)
        else:
            continue
    
loop()