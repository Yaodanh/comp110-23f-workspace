my_words: str = input("input a word: ")
letter_idx: int = int(input("input a integer: "))

def mimic_letter(my_words:str, letter_idx:int)-> str:
    """outputs the character of my_words at index letter_idx"""
    if len(my_words) <= letter_idx:
      return("Too high of an index") 
    else:
       return my_words[letter_idx] 
    
x: int = 120


pets: list[str] = ["Louie", "Bo", "Bear"]
for names in pets:
   print(f"Good boy, +{names}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range (0,len(names)):
   elem: str = names[idx]
   print(f"{idx}:{elem}")


