import os
from itertools import combinations
from affectationSPA import construct_ressources_list, lancement_testaffection_bruteforce
from hongrois import allouer_sujets
from mariage_stable import allocate_subjects_mariage
from readCsvMoodle import readCsvGenerateMoodle, lire_csv_et_generer_dictionnaires
from utils import assign_random, verification_nballocation_nbsujet, assign_choice
import time
from hongroisv2 import start_hongroisv2


def start_brute_force(dictionnaire_student_project, tableau_choix_possible):
    clesEtudiant = list(dictionnaire_student_project.keys())
    ressources = construct_ressources_list(tableau_choix_possible)

    # cette ligne peut poser probleme ( grand nombre de combinaisons)
    cl = list(combinations(ressources, len(clesEtudiant)))
    start_time = time.time()
    lancement_testaffection_bruteforce(cl, dictionnaire_student_project, clesEtudiant)
    end_time = time.time()
    print(f"Temps d'exécution bruteforce: {end_time - start_time} secondes")

    # print("\nTous les choix possibles de projet :", tableau_choix_possible)
    print(dictionnaire_student_project)


def start_hongrois(dictionnaire_student_project, tableau_choix_possible):
    start_time = time.time()
    allocations = allouer_sujets(dictionnaire_student_project, tableau_choix_possible)
    end_time = time.time()

    print("\nAllocations des sujets méthode hongroise :")
    chemin_sous_dossier = os.path.join(os.getcwd(), "resultatAllocation")

    chemin_fichier_resultat = os.path.join(chemin_sous_dossier, "resultatHongrois.txt")

    compteur = 0
    coutFinal = 0
    with open(chemin_fichier_resultat, 'w') as fichier:
        for etudiant, (sujet, choix) in allocations.items():
            print(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.")
            coutFinal = coutFinal + choix
            fichier.write(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.\n")
            compteur = compteur + 1
        print(f"cout final de la méthode hongroise -> {coutFinal}\n")
        fichier.write(f"cout final de la méthode hongroise -> {coutFinal}\n")
        verification_nballocation_nbsujet(tableau_choix_possible, compteur)
        print("\nTous les choix possibles de projet :", tableau_choix_possible)
        fichier.write(f"Tous les choix possibles de projet  \n{tableau_choix_possible}\n")
        fichier.write(f"dictionnaire_student_project  {dictionnaire_student_project}\n")
        print(f"Temps d'exécution hongrois: {end_time - start_time} secondes\n")
    return coutFinal


def start_mariage(dictionnaire_student_project, tableau_choix_possible):
    start_time = time.time()
    allocations, etudiants_non_attribues = allocate_subjects_mariage(dictionnaire_student_project,
                                                                     tableau_choix_possible)
    end_time = time.time()

    print("\nAllocations des sujets méthode des Mariages Stable :")
    chemin_sous_dossier = os.path.join(os.getcwd(), "resultatAllocation")

    chemin_fichier_resultat = os.path.join(chemin_sous_dossier, "resultatMariage.txt")

    compteur = 0
    coutFinal = 0
    with open(chemin_fichier_resultat, 'w') as fichier:
        for etudiant, (sujet, choix) in allocations.items():
            print(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.")
            coutFinal = coutFinal + choix
            # Écrire chaque ligne dans le fichier
            fichier.write(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.\n")
            compteur = compteur + 1
        if etudiants_non_attribues:
            print("\nCertains étudiant n'ont pas eu de projets attribué :")
            fichier.write(f"\nCertains étudiant n'ont pas eu de projets attribué :")
            for etudiant in etudiants_non_attribues:
                print(etudiant)
                fichier.write(f"{etudiant} n'a recu aucun sujet.\n")
        print(f"cout final de la méthode allocation des projets étudiants -> {coutFinal}\n")
        fichier.write(f"cout final de la méthode allocation des projets étudiants -> {coutFinal}\n")
        verification_nballocation_nbsujet(tableau_choix_possible, compteur)
        print("\nTous les choix possibles de projet :", tableau_choix_possible)
        fichier.write(f"Tous les choix possibles de projet  {tableau_choix_possible}\n")
        fichier.write(f"dictionnaire_student_project  {dictionnaire_student_project}\n")
        print("Temps d'exécution allocation des projets étudiants : ", end_time - start_time, " secondes\n")
    return coutFinal


''' ------------------------------------ '''


def main_test_developpeur(choix, algorithme, aleatoire_place, nbminplace, nbmaxplace):
    if choix == 1:
        # On utilise 2 dictionnaires pour les choix des étudiants et les places disponibles par projets.
        etudiants_burgers_dictionnaire, tableau_choix_possible = readCsvGenerateMoodle(
            'inputCSV/Election_du_Burger_Supr_me.csv')
        if aleatoire_place == 1:
            assign_random(tableau_choix_possible, nbminplace, nbmaxplace)  # entre min et max places
        else:
            assign_choice(tableau_choix_possible)
        # print("Tous les choix possibles de burgers :", tableau_choix_possible)
        # print(etudiants_burgers_dictionnaire)
        if algorithme == "fb":
            start_brute_force(etudiants_burgers_dictionnaire, tableau_choix_possible)
        elif algorithme == "hong":
            start_hongrois(etudiants_burgers_dictionnaire, tableau_choix_possible)
        else:
            start_mariage(etudiants_burgers_dictionnaire, tableau_choix_possible)

    elif choix == 2:
        etudiants_projects, tableau_choix_possible = lire_csv_et_generer_dictionnaires('inputCSV/instance0.csv')
        if aleatoire_place == 1:
            assign_random(tableau_choix_possible, nbminplace, nbmaxplace)  # entre min et max places
        else:
            assign_choice(tableau_choix_possible)
        if algorithme == "fb":
            start_brute_force(etudiants_projects, tableau_choix_possible)
        elif algorithme == "hong":
            start_hongrois(etudiants_projects, tableau_choix_possible)
        else:
            start_mariage(etudiants_projects, tableau_choix_possible)


def start_all(etudiants_dictionnaire, tableau_choix_possible):
    # start_brute_force(etudiants_dictionnaire, tableau_choix_possible)
    cout_hongrois = start_hongrois(etudiants_dictionnaire, tableau_choix_possible)
    cout_mariage = start_mariage(etudiants_dictionnaire, tableau_choix_possible)
    valeurs = [cout_mariage, cout_hongrois]
    valeurs.sort()
    print(f"affichage des couts finaux : {valeurs[0]} < {valeurs[1]}")


''' ------------------------------------ '''


# Main du projet


def main(developpeur_or_client, choix, algorithme, aleatoire_place, nbminplace, nbmaxplace):
    print("\n" * 10)

    # Affiche l'heure actuelle
    print(time.strftime("%H:%M:%S"))

    if developpeur_or_client == 0:
        main_test_developpeur(choix, algorithme, aleatoire_place, nbminplace, nbmaxplace)
    else:
        if choix == 1:
            filename = 'inputCSV/Election_du_Burger_Supr_me.csv'
            etudiants_dictionnaire, tableau_choix_possible = readCsvGenerateMoodle(filename)
            if aleatoire_place == 1:
                assign_random(tableau_choix_possible, nbminplace, nbmaxplace)
            else:
                assign_choice(tableau_choix_possible)
            start_all(etudiants_dictionnaire, tableau_choix_possible)
            # start_hongroisv2(filename,aleatoire_place,nbminplace,nbmaxplace)
        elif choix == 2:
            filename = 'inputCSV/instance0.csv'
            etudiants_dictionnaire, tableau_choix_possible = lire_csv_et_generer_dictionnaires(filename)
            if aleatoire_place == 1:
                assign_random(tableau_choix_possible, nbminplace, nbmaxplace)
            else:
                assign_choice(tableau_choix_possible)
            start_all(etudiants_dictionnaire, tableau_choix_possible)
        # start_hongroisv2(filename, aleatoire_place, nbminplace, nbmaxplace)


if __name__ == '__main__':
    aleatoire_place = 1
    nbminplace = 3
    nbmaxplace = 4
    developpeur_or_client = 1
    choix = 1
    algorithme = "osef"
    main(developpeur_or_client, choix, algorithme, aleatoire_place, nbminplace, nbmaxplace)
    # hongroisv2 peut être ignorer
