import random

# Choisir un chiffre aléatoire entre 0 et 100
int_guest: int = random.randint(0, 100)

print("Bievenue ! L'ordinateur à choisi un chiffre entre 0 et 100. Peux-tu le deviner ?")

# Compter le nombre de tentative de l'utilisateur
attempt_count = 0

# Faire une boucle qui va demander à l'utilisateur de deviner le chiffre.
# On lui demande autant de fois qu'il faut jusqu'à ce qu'il trouve.
while True:

    # Demander un chiffre à l'utilisateur
    user_guess: str = input("Ta suggestion: ")

    # Incrémentater le compteur de tentative
    attempt_count += 1

    # Vérifier que l'utilisateur a entré un chiffre.
    if not user_guess.isdigit():
        print("Je n'ai pas reconnu ta suggestion. Essai encore en entrant un chiffre entre 0 et 100.")
        continue

    # Convertir la suggestion de l'utilisateur en int
    user_guess = int(user_guess)

    # Vérifier que c'est le bon chiffre.
    if user_guess == int_guest:
        print("Bien joué! Tu as trouvé le bon chiffre !")
        break

    # Si ce n'est pas le bon chiffre, donné un indice à l'utilisateur.
    elif user_guess < int_guest:
        print("Trop petit !")
    elif user_guess > int_guest:
        print("Trop grand !")

# Afficher le nombre de tentative nécessaire pour trouver le chiffre.
print(f"Tu as trouvé le bon chiffre en {attempt_count} coups !")