from Hangman_visual import lives_visual_dict;
from Words import words
from random import randrange

random_word_index = randrange(0, len(words))
word = words[random_word_index]
word_len = len(word)
number_of_guesses_left = 7
list_of_letters = []
the_end = False
was_wrong_input = False
round = 0

for i in range(word_len):
    list_of_letters.append(".")

print("Welcome to Hangman Game. I generated random word and you have 7 chances to guess it. Good luck :)")

while not(the_end):
    round += 1
    print("ROUND " + str(round) + ".")
    if not(was_wrong_input):
        print("------------------------------------------------------------------------")
        print("Current State: You have " + str(number_of_guesses_left) + " attempts left")
        print(lives_visual_dict[number_of_guesses_left])
        print("------------------------------------------------------------------------")
        print("Guessed letters of word")
        print(list_of_letters)
        print("------------------------------------------------------------------------")

    print("If you want to try to guess a letter, type \"1\" and if you want to try to guess a word, type \"2\"")
    choice = input("Enter your choice: ")
    
    if not(choice.strip().isdigit()) or (int(choice) != 1 and int(choice) != 2):
        print("You did not enter a valide choice [" + choice + "]. Try again:")
        was_wrong_input = True
        continue
    elif int(choice) == 1:
        input_letter = input("Enter a letter: ")
        if not(input_letter.isalpha()) or len(input_letter) != 1:
            print("You did not enter a valide letter [" + input_letter + "]. Try again:")
            was_wrong_input = True
            continue
        
        guessed_at_least_one_word = False
        for i in range(word_len):
            if word[i].lower() == input_letter.lower():
                list_of_letters[i] = input_letter.upper()
                guessed_at_least_one_word = True

        are_all_letters_guessed = True

        for i in range(word_len):
            if list_of_letters[i] == ".":
                are_all_letters_guessed = False
                break

        if are_all_letters_guessed:
            print("Congratulation, you guessed a word [" + word + "]")
            the_end=True
        else:
            if not(guessed_at_least_one_word):
                number_of_guesses_left -= 1
                if number_of_guesses_left == 0:
                    print("The End, You had your 7 chances. You lose :P Secret word is " + word)
                    the_end=True
    elif int(choice) == 2:
        input_word = input("Enter a word: ")

        if input_word.upper() == word.upper():
            print("Congratulation, you guessed a word [" + word + "]")
            the_end=True
        else:
            print("Bad luck, you did not guessed a word")
            number_of_guesses_left -= 1
            if number_of_guesses_left == 0:
                print("The End, You had your 7 chances. You lose :P Secret word is " + word)
                the_end=True
    
    
    was_wrong_input = False