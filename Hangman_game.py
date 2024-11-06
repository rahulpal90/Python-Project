import random

Words = ["mumbai","delhi","kolkata","chennai","gorakhpur","thane","kalyan","mulund","dadar","banaras","mirzapur","kanpur","lucknow","patna","aasansol","nagpur","ayodhya","jabalpur","bhopal","vidisha","barabanki","Unao","jhasi","ujjain","itarsi"]

Word = random.choice(Words)

tota_chances = 3
guess_words = "-"*len(Word)

while tota_chances !=0:
    print(guess_words)
    letter = input("Guess the Letter: ").lower()
    if letter in Words:
        for index in range(len(Words)):
            if Words[index]==letter:
                guess_words = guess_words[:index]+letter+guess_words[index+1:]
                print(guess_words)
        if guess_words == Word:
            print("Congrats you Won")      
            break
        else:
            
            tota_chances -=1
            print("Incorrect Guess")  
            print(f"Total Remaing Chance : {tota_chances}")  
    else:
        print("Game Over")        
