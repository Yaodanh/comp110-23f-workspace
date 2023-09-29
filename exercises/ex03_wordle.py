"""ex03_wordle.py"""
__author__ = "703707593"


def contains_char(secret: str, guess_letter: str)->bool:
    """Search the guess_letter in the search string."""
    idx: int = 0
    assert len(guess_letter) == 1
    while idx < len(secret):
        if guess_letter == secret[idx]:
            return True
        idx = idx+1
    return False
         
def emojified(guess: str, secret: str)->str:
    """Search the guess string in the secret string."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result = ""
    idx :int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else: 
             result += WHITE_BOX
        idx += 1
    return (result)

    

def input_guess(expected_length)->int:
    """Prompt the player for a guess of expected length."""
    guess = input("What is your guess?" )
    while (len(guess) != expected_length):
        guess = input((f"That wasn't {expected_length} chars! Try again: "))
    if len(guess) == expected_length:
        return guess


def main()-> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 0
    secret:str = "codes"
    while turn_number <= 6:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print (f"You won in {turn_number}/6 turns!")
            return
        if guess != secret:
            turn_number += 1
            if turn_number == 6:
                print("6/6 - Sorry, try again tomorrow!")
main()