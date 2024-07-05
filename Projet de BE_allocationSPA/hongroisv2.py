import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from utils import assign_random, verification_nballocation_nbsujet, assign_choice


def lire_csv_et_construire_matrice(filename):
    df = pd.read_csv(filename)

    col_nom = df.columns[df.columns.str.contains('Nom complet', case=False)][0]
    cols_couts = df.columns[df.columns.str.contains('Burger', case=False)]
    if len(cols_couts) == 0:
        col_start_idx = df.columns.get_loc(col_nom) + 1
        cols_couts = df.columns[col_start_idx:]
    noms_taches = cols_couts.tolist()
    etudiants = df[col_nom].tolist()
    couts = df[cols_couts].replace(-1, np.inf).values
    couts = couts.astype(float)
    return etudiants, noms_taches, couts


def allouer_taches(etudiants, noms_taches, couts, places):
    n = len(etudiants)
    m = sum(places.values())
    cout_expanded = np.full((n, m), np.inf)
    col_index = 0


    for j, tache in enumerate(noms_taches):
        for place in range(places[tache]):
            cout_expanded[:, col_index] = couts[:, j]
            col_index += 1

    row_ind, col_ind = linear_sum_assignment(cout_expanded)

    allocations = {}
    for i, choix in enumerate(col_ind):
        etudiant = etudiants[row_ind[i]]
        tache_index = choix
        for tache, nb_places in places.items():
            if tache_index < nb_places:
                tache_assign = tache
                break
            tache_index -= nb_places
        cout = cout_expanded[row_ind[i], choix]
        allocations[etudiant] = (tache_assign, cout)

    cout_total = cout_expanded[row_ind, col_ind].sum()

    return allocations, cout_total


def start_hongroisv2(filename, assign_method, nbmin, nbmax):
    etudiants_instance0, noms_taches_instance0, couts_instance0 = lire_csv_et_construire_matrice(filename)
    places_instance = {tache: 0 for tache in noms_taches_instance0}
    if assign_method == 0:
        assign_choice(places_instance)
    else:
        assign_random(places_instance, nbmin, nbmax)
    allocations_instance, cout_total_instance0 = allouer_taches(etudiants_instance0, noms_taches_instance0,
                                                                couts_instance0, places_instance)
    print("Allocations des tâches méthode hongroise :")
    for etudiant, (tache, cout) in allocations_instance.items():
        print(f"{etudiant} a été alloué à la tâche {tache} avec un coût de {cout}.")
    print(f"Coût total minimal : : {cout_total_instance0}")


start_hongroisv2('inputCSV/Election_du_Burger_Supr_me.csv', 1, 2, 2)

''''
# Exemple d'utilisation avec burger.csv
filename_burger = 'inputCSV/Election_du_Burger_Supr_me.csv'
etudiants_burger, noms_taches_burger, couts_burger = lire_csv_et_construire_matrice(filename_burger)
places_burger = {tache: 0 for tache in noms_taches_burger}  
assign_random(places_burger, 4, 4)
allocations_burger, cout_total_burger = allouer_taches(etudiants_burger, noms_taches_burger, couts_burger, places_burger)

print("Allocations des tâches méthode hongroise pour burger.csv :")
for etudiant, (tache, cout) in allocations_burger.items():
    print(f"{etudiant} a été alloué à la tâche {tache} avec un coût de {cout}.")
print(f"Coût total minimal pour burger.csv : {cout_total_burger}")
'''
