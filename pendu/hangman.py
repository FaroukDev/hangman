'''
'Etape 1 :
Importer une Liste de potence
Choisir le mot aléatoire
Definir la taille du mot
Nombre de lettre trouvé
Nombre d'echec = 0

Etape 2
Do Voulez vous jouer Y/N
  Tant que nbre echec < 5 OR Nombre de lettre à trouver
    Tant que l'utilisateur ne rentre pas un caractere
        Demander à l'utilisateur seulement un caractere,

    Convertir ce caractere
    Si la lettre existe 
    word_to_find le mot :
        afficher le mot caché mise à jour avec l'emplacement
    SiNo
        Afficher la potence corespendante
        incrementer nombre echec ++

  Si nombre tentative ==0
     écrire Perdu


 Class Pendu
    attribbut : mot à deviner,
    attribut nbre de tentative restantes
    attribut  nbre d'échec


    Définir les variables
    fonction recupérer le mot
    fonction vérifier si la lettre existe 
    word_to_find le mot
    fonction récuperer la lettre
    fonction (nbre d'eche)
        print potence
'''

#from random_word import RandomWords

#r = RandomWords()

# r.get_random_word()

import pendu
import logging
import datetime
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_format = '%(asctime)s %(filename)s: %(message)s'
logging.basicConfig(filename="hangman.log", format=log_format,
                    datefmt='%Y-%m-%d %H:%M:%S')

logger.info("information message")


#f = open("./pendu/hang.py", "r")
#stages = f.read()
#print(stages)
stages = [ """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     /
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |      |
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |
            |
            |
            -
            """,
            """
            --------
            |      |
            |      
            |
            |
            |
            -
            """
]

def main():
    guesses = []
    count = 1
    word_to_find = "farouk"
    word = []


    while count < 7:
        guess = input('guess a letter: ')
        guesses.append(guess)
        print(guesses)
        if ''.join(guesses) == word_to_find:
            print(word)
            print('you win')
            break
        elif word == guesses:
            print('you win')
            break
        else:
            for char in word_to_find:
                if len(guess) == len(stages) - 1:
                    word.append(char)
                    print(char)
                    print(stages)
                else:
                    print('_')
            count += 1
    else:
        print('\nyou lose')
    print(guesses)

    logging.info("script ended")
