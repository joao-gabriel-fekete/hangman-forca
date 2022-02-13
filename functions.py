
import requests
def getWord():
    
    serverCheck = requests.get('https://random-words-api.vercel.app/word')
    if serverCheck.status_code != 200:
        print("Há um problema com o servidor. Tente novamente mais tarde.")
        return

    info = ""
    while len(info) <= 2:
        responseWeb = requests.get('https://random-words-api.vercel.app/word')
        
        info = responseWeb.json()[0]

    return info


