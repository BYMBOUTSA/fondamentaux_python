from multiprocessing.spawn import _main
from tkinter.tix import MAIN
from pip import main

"""
    def allele_combinations(genotype: str) -> list[str]:
    possibilities = []
    for r in genotype[:2]:
        for y in genotype[2:]:
            possibility = r + y

            if possibility not in possibilities:
                possibilities.append(possibility)
    return possibilities

"""


def allele_combinations(genotype: str) -> list: 
    """
        Doc de la fonction...
    """  
    return sorted(list(set([r + y for r in genotype[:2] for y in genotype[2:]])))


"""
Ecrire une fonction qui prend en argument 2 génotypes de 
parents et qui retourne les génotypes possibles des enfants. Vous,
pouvez utiliser la fonction de la question 1 pour construire cette fonction.
Exemple avec 2 parents RrYy:
"""

def genotype_probabilities(parent_1: str, parent_2: str) -> dict:
    allele_combi_1 = allele_combinations(parent_1)
    allele_combi_2 = allele_combinations(parent_2)

    # allele_combi_1 = ['RY','Ry', 'rY', 'ry']
    # allele_combi_2 = ['RY','Ry', 'rY', 'ry']

    probabilities = {}

    total = 0

    for p1 in allele_combi_1:
        for p2 in allele_combi_2:

            # p1 = "RY"
            # p2 = "RY"
            child_geno = ""
            for x, y in zip(p1, p2):
                child_geno += x + y if x.isupper() else y + x
            if child_geno not in probabilities.keys():
                probabilities[child_geno] = 1
            else:
                probabilities[child_geno] += 1
            total += 1

    for k, v in probabilities.items():
        probabilities[k] = v / total

        print(f"{k} : {v} / {total}")

    return probabilities


"""
Faire une fonction qui retourne le génotype le plus probable de
l'enfant des 2 génotypes parents donnés en arguments. Vous pouvez utiliser
la fonction de la question 3 pour construire cette fonction.
"""

def most_probable_genotype(parent_1: str, parent_2: str) -> str:
    probabilities = genotype_probabilities(parent_1, parent_2)

    most_probable = ""
    max_proba = 0

    for genome, proba in probabilities.items():
        if proba > max_proba:
            max_proba = proba
            most_probable = genome
    return most_probable


if __name__ == "__main__":
    print("Le génotype enfant le plus probable est:", most_probable_genotype("RrYy", "RrYy"))
       