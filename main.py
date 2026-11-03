import json
import requests
api_key="https://random-word-api.herokuapp.com/word?number=5"

# word =["keep","humble","curiosity","optimal","efficient"]
check=0
new_words = []
def check_previousword():
   while len(new_words)<5:
    response =requests.get(api_key)
    word =response.json()
    for w in word:
        if w not in data and w not in new_words : # te word should not in data and shoulc not in new_words
            new_words.append(w)
            if len(new_words)==5:
                break
   return new_words


def toget_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response1 = requests.get(url)
    meaning_data = response1.json()
    print(meaning_data)
    if 'title' in meaning_data:
        print(" the meaning was not found")
        return
        
    print(meaning_data[0]["meanings"][0]["definitions"][0]["definition"])
  

#to get the word 
def word_s(new_words):
    print(f"Todays word is'{new_words[check]}' !!!")
    toget_meaning(new_words[check])
    sentence=input(f"Enter the sentence that have the '{new_words[check]}':")
    return sentence

# to check the word is there in sentence
def check_wordIn_sentence(new_words,user_sentence):
    
    while new_words not in user_sentence:
        user_sentence=input(f"Try again ! your sentece is wrong use '{new_words}'in your sentence :")
    print("Perfect your sentese is correct")
    if check <len(new_words)-1:
        print("Now next word")
    return user_sentence
   
data={} # empty dict 

def to_store_words():
     data.update({new_words[check] :user_sentence} )
     with open("daily_words.json","w") as file: # file 
         json.dump(data,file)


#to get to know 
def to_know_learned_words():
    with open("daily_words.json","r")as file:
        previous_words=json.load(file)
        data.update(previous_words)
        
        print("the word which we learned are :\n ")
        for i,(word,sentence) in enumerate(data.items(), start=1):
            print(f"{i}.{word}")
            print(f" Sentence :{sentence}") 
        
# data.items() gives you both the word (key) and sentence (value).
# enumerate() adds numbering.

  #for end of day       
def end_ofday():
    bye= "\nThat is it for todays bye!! come tomorrow to do more 5 words"
    return bye




     
# main part of code
to_know_learned_words()
new_words= check_previousword()
print("\n The words for todays are :")
print(new_words)

for check in range (5):
    user_sentence=word_s(new_words)
    user_sentence=check_wordIn_sentence(new_words[check],user_sentence)  
    to_store_words()   
    

print(end_ofday())   

