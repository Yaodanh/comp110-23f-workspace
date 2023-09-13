"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730707593"

five_character_word: str = input ("Enter five-character word:")
single_character:str=input("Enter a single character :" )
print("Searching for"  + five_character_word +  "in"  + single_character)

if len(five_character_word) != 5:
    print ("Error: Word must contain 5 characters")
    exit()

if len(single_character) != 1:
    print ("Error: Character must be a single character.")
    exit()

if single_character == five_character_word[0]:
    print(single_character + " found at index 0")

if single_character== five_character_word[1]:
     print(single_character + " found at index 1")

if single_character == five_character_word[2]:
    print(single_character + " found at index 2")

if single_character == five_character_word[3]:
    print(single_character + " found at index 3")

if single_character == five_character_word[4]:
    print(single_character + " found at index 4")

instance: int=0

if single_character == five_character_word[0]:
    instance = instance + 1
else:
    instance = instance

if single_character == five_character_word[1]:
   instance = instance + 1
else: instance = instance

if single_character == five_character_word[2]:
   instance = instance + 1
else: instance = instance

if single_character == five_character_word[3]:
   instance = instance + 1
else: instance = instance

if single_character == five_character_word[4]:
   instance = instance + 1
else: instance = instance

print (str(instance)+ " instances of " + single_character + "found in " + five_character_word)

