import json
word =["keep","humble","curiosity","optimal","efficient"]
check=0


def word_s(word):
    print(f"Todays word is'{word[check]}' !!!")
    sentence=input(f"Enter the sentence that have the '{word[check]}':")
    return sentence

def check_wordIn_sentence(words,user_sentence):
    
    while words not in user_sentence:
        user_sentence=input(f"Try again ! your sentece is wrong use '{words}'in your sentence :")
    print("Perfect your sentese is correct")
    if check <len(word)-1:
        print("Now next word")
          
         
def end_ofday():
    bye= "\nThat is it for todays bye!! come tomorrow to do more 5 words"
    return bye
    


for check in range (5):
    user_sentence=word_s(word)
    check_wordIn_sentence(word[check],user_sentence)  
    data={
       data.update({word[check] :user_sentence} )
       }
  
    with open("daily_words.json","w") as file:
     json.dump(data,file)

print(end_ofday())   


