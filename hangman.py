import random
import string
from words import words


def generate_word():
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = generate_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_words = set()
    lives = len(word)

    while len(word_letters) > 0 and lives > 0:
        print('Used words ', ' '.join(used_words))
        words_list = [letter if letter in used_words else '-' for letter in word]
        #
        # for letter in word:
        #     if letter in used_words:
        #         words_list.append(letter)
        #     else:
        #         words_list.append('-')

        print('Current words: ', ' '.join(words_list))

        user_letter = input('Guess a letter ').upper()
        if user_letter in alphabet - used_words:
            used_words.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_words:
            print('You have used this word already. Try again')

        else:
            print('You put an invalid word. Try again')

        lives -= 1

    if lives == 0:
        print('You lost ^^')
    else:
        print('Yeah, you guessed this word: ', word)


hangman()
