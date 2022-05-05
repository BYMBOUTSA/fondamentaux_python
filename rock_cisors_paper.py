import random
from typing import Tuple

options: dict = {
    "r": "rocher",
    "c": "ciseau",
    "p": "papier"
}

user_score: int = 0
computer_score:int = 0

def play(options: dict, user_score: int, computer_score: int) -> Tuple:
    """
        Faire la docstring
    """

    user_input: str = input("Quel est ton choix ? (r/c/p) ")
    computer_input: str = random.choice(list(options.keys()))

    while user_input not in options.keys():
        print("Je n'ai pas compris ton choix.")
        user_input = input("Choisi entre 'r', 'c' et 'p': ")

    print(f"Tu as choisi: {options[user_input]}")
    print(f"L'ordi a choisi: {options[computer_input]}")

    gagnant = [('r', 'c'), ('c', 'p'), ('p', 'r')]

    if (user_input, computer_input) in gagnant:
        print("Tu as gagné !")
        user_score += 1
    elif user_input == computer_input:
        print("Egalité")
    else:
        print("Tu as perdu")
        computer_score += 1

    return (user_score, computer_score)

def ask_turn_number(q: str) ->int:
    turns: str = input(q)

    while not turns.isdigit():
        turns = input("Nombre de tours non reconnus. Choisi un chiffre impair stp: ")

    return int(turns)

turns: str = ask_turn_number("Combien de tours souhaites-tu jouer ? (doit être impair) ")

while turns % 2 == 0:
    turns = ask_turn_number("Désolé, le chiffre que tu as choisi n'est pas impair. Choisi un autre chiffre pls: ")

while user_score == computer_score:
    for i in range(turns):
        user_score, computer_score = play(options, user_score, computer_score)
    
    print(f"Score: {user_score} / {computer_score} (toi / ordinateur).")

    if user_score == computer_score:
        print("Egalité ! Jouez 2 tours de plus pour vous départager.")

    # Relance tours de plus si égalité
    turns = 2
    


# En le faisant simplement sans utiliser la liste des tuples des gagants
"""if user_input == "r" and computer_input == "c":
    print("Tu as gagné !")
    user_score += 1

elif user_input == "c" and computer_input == "p":
    print("Tu as gagné")
    user_score += 1
elif user_input == "p" and computer_input == "r":
    print("Tu as gagné")
    user_score += 1
elif user_input == computer_input:
    print("Egalité")
else:
    print("Tu as perdu")
    computer_score += 1 """


print(f"Tu as gagné la partie !" if user_score > computer_score else "Tu as perdu !")

