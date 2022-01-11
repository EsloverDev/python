import os
import random


IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = ['Sello', 'Censura', 'Vena', 'Espinacas', 'Plastica',
         'Linterna', 'Mapamundi', 'Hipopotamo', 'Arma', 'Pluma']


def clear_screen():   
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def random_word():
    word = random.choice(WORDS)
    return word.upper()


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('........................................')


def run():
    word = random_word()
    secret_word = ['_']*len(word)
    clear_screen()
    print('COMIENZA EL JUEGO --->', '')
    tries = 0
    while True:
        if tries == len(IMAGES):
            break
        display_board(' '.join(secret_word), tries)
        letter = str(input('Digite un letra: ')).upper()

        letter_indexe = []
        for idx in range(len(word)):
            if letter == word[idx]:
                letter_indexe.append(idx)

        if len(letter_indexe) == 0:
            tries += 1
        else:
            for idx in letter_indexe:
                secret_word[idx] = letter
                if ''.join(secret_word) == word:
                    print('GANASTE')

    print('FIN DEL JUEGO')


if __name__ == '__main__':
    run()