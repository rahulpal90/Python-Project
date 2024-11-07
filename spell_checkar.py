# Importing Libary spell_check
from spellchecker import SpellChecker                                                    # Libary Import ki SpellChecker ki

# creating Class
class spell_checkerapp:                                                                   # Ek Class Banai Spell_Checker Naam ki
    def __init__(self) -> None:
        self.spell = SpellChecker()                                                             
        
    def correct_text(self,text):                                                           # Function Create kiya correct_text naam ka                                 
        words = text.split()
        correct_words = []
        
        for word in words:                                                                 # for Loop challaya jo words ko test kar ta rahai ga or correct ho nay k baad append (Add) kare ga correct_word may
            correct_word = self.spell.correction(word)
            if correct_words != word.lower():
             print(f"correcting'{word}' to '{correct_word}'") 
             correct_words.append(correct_word)
             
        #Returing the Correct text                                                            # run Fun. banaya sahi Spelling return kare ga 
        return' '.join(correct_words) 
    def run (self):
        print("\n----Spell Checkar----")
        
        while True:                                                                          # Fir while loop laga jo bar bar user ko puch ta rahai spelling jab user Quit kar dyr Exit lik kar
            text =input("Enter Text to check (or Type Exit to Quit):")
            
            if text.lower() == "exit":
                print("Closing....")
                break
            
            corrected_text = self.correct_text(text)
            print(f"Corrected Text : {corrected_text}")
            
# Running Main Program                                                                           # yee main program ko call kiya Run ho nay k liye .
if __name__ == "__main__":
    spell_checkerapp().run()                  
