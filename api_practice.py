# requests.get() sends a GET request to a URL.
#.status_code tells us whether the request was successful.

""" For example:
- 200 → Successful request.
- 404 → Resource not found.
- 500 → Server error."""
# response.json() → Gets JSON data directly from an API response.

import requests
# api_key="https://random-word-api.herokuapp.com/word?number=5"
# response =requests.get(api_key)
# word =response.json()
# print(response.status_code) 
# print(word)
# print(type(word))
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# url = "https://api.dictionaryapi.dev/api/v2/entries/en/curiosity"

# response = requests.get(url)
# meaning_data = response.json()

# print(meaning_data)
# print("================")
# print(meaning_data[0].keys())
# print("================")
# print(meaning_data[0]["meanings"])
# print(meaning_data[0]["meanings"][0].keys())
# print(meaning_data[0]["meanings"][0]["definitions"][0]["definition"])

def toget_meaning(word):
    openai_api_key = os.getenv("OPENAI_KEY")
    message=[{"role":"system","content":"you are an english vocabulary teacher that provide"
    "meaning ,part of speech and example"},
    {"role":"user","content":f"give meaing on this {word}"}]
    openai=OpenAI(api_key=openai_api_key)
    response1=openai.chat.completions.create(model="gpt-4o-mini",messages=message)
    return response1.choices[0].message.content
name ="curiosity"
name1=toget_meaning(name)
print(name1)