#  linux/Mac
- cd Projet_N16
- ./setupPenv.sh
- source venv/bin/activate
- cd Projet de Be_allocationSPA
- Python3 intergraphique.py

#  Windows (via PowerShell) :
- cd Projet_N16
- bash setupPenv.sh
- .venv/Scripts/Activate.ps1
- cd Projet de Be_allocationSPA
- Python3 intergraphique.py


In the main.py file, if you don't want to use the graphical interface : \
if name == 'main':
    For each project, define a place between 5 and 7, for example ( random ) \
    aleatoire_place = 1 <--- 0 to choose places by hand and 1 to choose places between nbmin and nbmaxplace aléatoire \
    nbminplace = 3 <--- places per project minimum \
    nbmaxplace = 4 <--- maximum places per project. \
    developper_or_client = 1 <--- 0 if to display case by case for developer in console otherwise 1 for client. \
    choice = 1 <--- 1 = moodle file 2 = instanceGénéree. \
    algorithm = "osef" <--- "fb" or "hong" or "mariage" ( or "ALL" to run all algorithms) \
    main(developpeur_or_client, choix, algorithme,aleatoire_place,nbminplace,nbmaxplace) 





# Vous pouvez tester 2 fichiers celui du moodle ou de l'instance (lancer le fichier spa_instance) pour générer
Dans le fichier main.py pour ne pas utiliser l'interface graphique : \
if __name__ == '__main__': \
    Par projet il faut définir une place entre 5 et 7 par exemple ( aléatoire ) \
    aleatoire_place = 1  <---  0 pour choisir à la main les places et 1  pour choisir les places entre nbmin et nbmaxplace aléatoire \
    nbminplace = 3  <--- places par projet minimum \
    nbmaxplace = 4   <--- places maximum par projet.  \
    developpeur_or_client = 1    <---  0 si pour afficher cas par cas pour le développeur dans la console sinon 1 pour client.  \
    choix = 1    <---  1 = fichier moodle 2 = instanceGénéree.  \
    algorithme = "osef"     <--- "fb" ou "hong" ou "mariage"  ( ou "ALL" pour  lancer tous les algorithmes)  \
    main(developpeur_or_client, choix, algorithme,aleatoire_place,nbminplace,nbmaxplace)   



