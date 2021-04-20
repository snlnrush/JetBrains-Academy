# Write your code here
import random

lst = ['python', 'kotlin', 'java', 'javascript']
random.shuffle(lst)

comp_choice = lst[0]

#comp_choice = 'python'
set_comp_choice = set(comp_choice)

print('H A N G M A N')


hid_word = ['-' for x in range(len(comp_choice))]

lifes = 8
guessed_letters = 0
set_guessed = set()

while True:
    status = input('Type "play" to play the game, "exit" to quit: ')
    if status == 'exit':
        break
    elif status != 'exit' and status != 'play':
        continue
    else:
        while lifes > 0:
            print()
            print(''.join(hid_word))
            if guessed_letters == len(hid_word):
                print('You guessed the word!')
                print('You survived!')
                break
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print('You should input a single letter')
                continue
            if not letter.isalpha() or not letter.islower():
                print('Please enter a lowercase English letter')
                continue
            # if letter in set_comp_choice and letter in set_guessed:
            if letter in set_guessed:
                # print('No improvements')
                # lifes -= 1
                print("You've already guessed this letter")
                continue
            if letter not in set_comp_choice and letter not in set_guessed:
                set_guessed.add(letter)
                lifes -= 1
                print("That letter doesn't appear in the word")
                continue
            elif letter in set_comp_choice:
                set_guessed.add(letter)
                for idx, let in enumerate(comp_choice):
                    if let == letter:
                        hid_word[idx] = let
                        guessed_letters += 1

            else:
                print("That letter doesn't appear in the word")
                lifes -= 1
        else:
            print("You lost!")
