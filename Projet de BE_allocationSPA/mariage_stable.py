def allocate_subjects_mariage(etudiants_dictionnaire, tableau_choix_possible):
    etudiants = list(etudiants_dictionnaire.keys())
    sujets = list(tableau_choix_possible.keys())

    places_restantes = {sujet: tableau_choix_possible[sujet] for sujet in sujets}
    etudiants_disponibles = etudiants.copy()  # Utilisation d'une copie de la liste des étudiants
    allocation_temporaire = {}
    etudiants_non_attribues = []

    while etudiants_disponibles:
        etudiant = etudiants_disponibles.pop(0)  # Retirer le premier étudiant de la liste
        preferences = etudiants_dictionnaire[etudiant]
        preference_attribuee = False

        for sujet in preferences:
            if places_restantes[sujet] > 0:
                allocation_temporaire[etudiant] = sujet
                places_restantes[sujet] -= 1
                preference_attribuee = True
                break

        if not preference_attribuee:
            etudiants_non_attribues.append(etudiant)

    allocations = {}
    for etudiant, sujet in allocation_temporaire.items():
        rang_choix = etudiants_dictionnaire[etudiant].index(sujet) + 1
        allocations[etudiant] = (sujet, rang_choix)

    return allocations, etudiants_non_attribues