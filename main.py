import json
word =["keep","humble","curiosity","optimal","efficient"]
check=0

#to get the word 
def word_s(word):
    print(f"Todays word is'{word[check]}' !!!")
    sentence=input(f"Enter the sentence that have the '{word[check]}':")
    return sentence
# to check the word is there in sentence
def check_wordIn_sentence(words,user_sentence):
    
    while words not in user_sentence:
        user_sentence=input(f"Try again ! your sentece is wrong use '{words}'in your sentence :")
    print("Perfect your sentese is correct")
    if check <len(word)-1:
        print("Now next word")
    return user_sentence   
data={} # empty dict 
def to_store_words():
     data.update({word[check] :user_sentence} )
     with open("daily_words.json","w") as file: # file 
         json.dump(data,file)


#to get to know 
def to_know_learned_words():
    with open("daily_words.json","r")as file:
        previous_words=json.load(file)
        print(previous_words)
        
    
  #for end of day       
def end_ofday():
    bye= "\nThat is it for todays bye!! come tomorrow to do more 5 words"
    return bye
     
# main part of code

for check in range (5):
    user_sentence=word_s(word)
    user_sentence=check_wordIn_sentence(word[check],user_sentence)  
    to_store_words()   
    
to_know_learned_words()
print(end_ofday())   


