# This Project Fetch the Top 10 News from the newsapi.org and read the news aloud 
# my news api key = c0d27336a57644b681b96c35b79fc89b

import requests
import json

def speak(str):
    from win32com.client import Dispatch  # Using module for speak functionality

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)




if __name__ == '__main__':
    
    # URL = by using get method we get response from newsapi.org by using my api key

    url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=c0d27336a57644b681b96c35b79fc89b')
    response = requests.get(url)
    
    # converting the respose into JSON
    var = response.json()
    

    count = 0
    for i in range(10):
        # Accesing the Titles 
        var1 = var["articles"][i]["title"]

        string = f"Top News Headline {i+1} is {var1}"

        speak(string)
        
    
