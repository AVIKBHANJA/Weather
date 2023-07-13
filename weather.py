# pip install gtts(google text-to-speach)
# import any free weather api ,use endpoint url and api kay at the place of API
import requests
from gtts import gTTS
import json
import os

language='en'

city=input("enter the name of the city :\n")

url=f"https://api.weatherapi.com/v1/current.json?key=ff84356b78894208af9170741232506&q={city}"

r=requests.get(url)


wdic = json.loads(r.text)
temp_tospeak=wdic["current"]["temp_c"]
print(temp_tospeak)
# output for speaking
speak_weather=f"now the temparature of {city} is {temp_tospeak}"
output=gTTS(text=speak_weather,lang=language,slow=False)
print(r.text)
output.save("weatheraudio.mp3")
os.system("start weatheraudio.mp3")
