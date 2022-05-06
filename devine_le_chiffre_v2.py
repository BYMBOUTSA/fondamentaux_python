# Le but est de faire jouer l'ordinateur.

import random

# Choisir un chiffre aléatoire entre 0 et 100
int_guess: int = random.randint(0, 100)

print("Bievenue ! Un chiffre a été choisi de façon aléatoire entre 0 et 100. Peux-tu le deviner avant l'ordinateur ?")

# Compter le nombre de tentative de l'utilisateur
attempt_count: int = 0

# Les possibilitées de l'ordinateur.
computer_options: list = list(range(101))

# Booléen pour savoir à qui c'est le tour de jouer
my_turn: bool = True

# Faire une boucle qui va demander à l'utilisateur de deviner le chiffre.
# On lui demande autant de fois qu'il faut jusqu'à ce qu'il trouve.
while True:

    if my_turn:
        # Demander un chiffre à l'utilisateur
        user_guess: str = input("Ta suggestion: ")

        # Incrémentater le compteur de tentative
        attempt_count += 1

        # Vérifier que l'utilisateur a entré un chiffre.
        if not user_guess.isdigit():
            print("Je n'ai pas reconnu ta suggestion. Essai encore en entrant un chiffre entre 0 et 100.")
            continue

        # Convertir la suggestion de l'utilisateur en int
        user_guess: int = int(user_guess)

    else:
        user_guess: int = random.choice(computer_options)
        print("L'ordinateur choisi:", user_guess)

    # Vérifier que c'est le bon chiffre.
    if user_guess == int_guess:
        print(f"Bien joué! Le bon chiffre était {int_guess}.")
        break

    # Si ce n'est pas le bon chiffre, donné un indice à l'utilisateur.
    elif user_guess < int_guess:
        print("Trop petit !")

        if user_guess in computer_options:
            # Pareille que celle avec l'user_guest_index
            # computer_options = [i for i in computer_options if i > user_guess]
            user_guess_index = computer_options.index(user_guess) + 1
            computer_options = computer_options[user_guess_index:]

    elif user_guess > int_guess:
        print("Trop grand !")

        if user_guess in computer_options:
            user_guess_index = computer_options.index(user_guess)
            computer_options = computer_options[:user_guess_index]

    # Donner le tour au prochain joueur
    my_turn = not my_turn

# Afficher le nombre de tentative nécessaire pour trouver le chiffre.
if my_turn:
    print("Bien joué ! Tu as trouvé le bon chiffre en ", attempt_count, "coups et avant l'ordinteur !")
else:
    print("L'ordinateur gagne ! Il a trouvé le bon chiffre en", attempt_count, "coups et avant toi !")