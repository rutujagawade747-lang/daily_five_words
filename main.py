import json
import requests
api_key="https://random-word-api.herokuapp.com/word?number=5"
response =requests.get(api_key)
word =response.json()
# word =["keep","humble","curiosity","optimal","efficient"]
check=0

def check_previousword():
    new_words = []
    for w in word:
        if w not in data and w not in new_words : # te word should not in data and shoulc not in new_words
            new_words.append(w)
    return new_words
   
#to get the word 
def word_s(new_words):
    print(f"Todays word is'{new_words[check]}' !!!")
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
        print(data)
        
    
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

