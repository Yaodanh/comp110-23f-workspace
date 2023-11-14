"""ex02_one_shot_wordle.py"""

__author__ = "703707593"

six_letter_guess: str =  input("What is your 6-letter guess?")

secret: str = "python"

idx: int = 0
ans: str = ""


   

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"



while len(six_letter_guess) != len(secret):
    six_letter_guess = input("That was not 6 letters! Try again:")
   

while idx < len(secret):
    if six_letter_guess[idx] == secret[idx]:
        ans += GREEN_BOX
    else: 
        found: bool = False
        new_index: int = 0
        while new_index < len(secret):
            if six_letter_guess[idx] == secret[new_index]:
                found = True
            new_index += 1
        if found == False:
            ans += WHITE_BOX
        else:
            ans += YELLOW_BOX
    idx += 1
print(ans)
if six_letter_guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!") 



