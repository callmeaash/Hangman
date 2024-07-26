import random
import sys
import argparse
from words import vegetable, fruit
parser = argparse.ArgumentParser(description='Hangman gameeeeeeee!!!', usage='%(prog)s -c fruit')
parser.add_argument('-c','--category', help='choose category of questions either fruit or vegetable', required=True)
arg =[]
arg = parser.parse_args()
categories = {
    'fruit': fruit,
    'vegetable': vegetable
}
print("\nHANGMAN GAME\n")

chosen_category = categories[arg.category]
word = random.choice(chosen_category).upper()
word_representation = ["__"] * len(word)
letters = list(word)
show = random.randint(0,3)
word_representation[show] = word[show]
revealed_indices = [show]
def game():
    life = 6
    while True:
        print()
        for letter in word_representation:
            print(f'{letter}\t', end="")

        if letters == word_representation:
            print("\n\nCorrect Guess")
            sys.exit()

        if life == 0:
            print("\n\nYou Lose")
            print(f'Correct Answer: {word}')
            sys.exit()


        user = input("\n\nGuess a letter: ").upper()
        found = check_letter(user)
        if found == False:
            life -= 1
        
        draw_hangman(life)

        
def check_letter(user):
    found = False
    for index, letter in enumerate(letters):
        if user == letter and index not in revealed_indices:
            word_representation[index] = letter
            revealed_indices.append(index)
            found = True
    return found

def draw_hangman(chances):
    if chances == 6:
        print("________ ")
        print("|  | ")
        print("|  ")
        print("|  ")
        print("|  ")
        print("|  ")
    elif chances == 5:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("|  ")
        print("|  ")
        print("|  ")
    elif chances == 4:
        print("________ ")
        print("|   | ")
        print("|   0 ")
        print("|  / ")
        print("|  ")
        print("|  ")
    elif chances == 3:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif chances == 2:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| ")
        print("| ")
    elif chances == 1:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| / ")
        print("| ")
    elif chances == 0:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| / \ ")
        print("| ")


game()
