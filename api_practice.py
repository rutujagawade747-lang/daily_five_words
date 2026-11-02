# requests.get() sends a GET request to a URL.
#.status_code tells us whether the request was successful.

""" For example:
- 200 → Successful request.
- 404 → Resource not found.
- 500 → Server error."""
# response.json() → Gets JSON data directly from an API response.

import requests
api_key="https://random-word-api.herokuapp.com/word?number=5"
response =requests.get(api_key)
word =response.json()
print(response.status_code) 
print(word)
print(type(word))