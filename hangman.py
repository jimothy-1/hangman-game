import random

word_bank = ['python', 'programming', 'games', 'program']
item_in_bank = random.randint(0, len(word_bank)-1) 
word = word_bank[item_in_bank]

blank_character = ' _ '
guessed_word = [blank_character for i in range(len(word))]

has_won = False

def get_puzzle(guess):

    counter = 0

    guessed_word_string = ''

    for letters in word:
        if guessed_word[counter] != blank_character:
            counter += 1
            continue
        elif guess == letters:
            guessed_word[counter] = ' '+ guess + ' '

        counter+=1
    
    guessed_word_string = ("").join(guessed_word)

    print(guessed_word_string)

    guessed_word_string = guessed_word_string.replace(" ", "")

    if guessed_word_string == word:
        print("You won!")
        return True
    else:
        return False

def get_guess():
    guess = input("Guess:")
    return guess


print(("").join(guessed_word))
while not has_won:
    guess = get_guess()
    has_won = get_puzzle(guess)
