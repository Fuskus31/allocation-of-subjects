import random
from datetime import datetime
from tkinter import simpledialog


def assign_random(choices, a, b):
    for choice in choices:
        choices[choice] = random.randint(a, b)


def assign_choice(choices):
    for choice in choices:
        user_input = simpledialog.askinteger("Input", f"Entrez le nb place à ajouter pour le choix {choice}:")
        if user_input is not None:  # si l'utilisateur clique sur cancel
            choices[choice] = user_input


def verification_nballocation_nbsujet(tableau_choix_possible, compteur):
    print(f"{sum(tableau_choix_possible.values())}  place disponibles {compteur} alloué")
    print(sum(tableau_choix_possible.values()) >= compteur)


def ecrire_matrice_hongroistxt(matrice_cout):
    heure_actuelle = datetime.now().strftime("%H:%M:%S")
    with open('resultatAllocation/matrice_cout_hongrois.txt', 'w') as f:
        f.write(f"Heure actuelle : {heure_actuelle}\n")
        for line in matrice_cout:
            formatted_line = ' '.join(f"{val:2d}" for val in line)
            f.write(formatted_line + '\n')

    print("La matrice de coût a été enregistrée dans 'matrice_cout_hongrois.txt'.")
