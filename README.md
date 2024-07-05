# BE allocation: an optimized approach to improve student subject allocation results.

## Allocating BE to students is an important task, as these projects allow students to increase their knowledge and gain experience that may help them decide to pursue a Master's degree. However, we need to allocate BE to students in a way that satisfies the maximum number of people.

Existing methods, such as "first come, first served" or random allocation, do not take into account students' preferences for specific projects. This mismatch can lead to unsuitable placements, hindering student learning and project success. It is therefore essential to develop a more efficient and equitable assignment system.
This research aims to analyze the shortcomings of existing methods and propose an alternative solution using an optimized algorithm. This algorithm will take into account students preferences for the projects, in order to create a more appropriate and mutually beneficial selection process.
We want to create an interface that allows the user to create different scenarios to compare different algorithms. The customer will be able to create his own scenarios and choose which algorithm he wants to use.



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
    main(developpeur_or_client, choix, algorithme,aleatoire_place,nbminplace,nbmaxplace)  \


We can choose if we want to select the number of places per project manually or automatically using our functions.
We can also choose to launch all allocation methods or not, with the choice of developer or client mode, with the moodle file or the generated instance.


<img width="347" alt="Screenshot 2024-06-05 at 17 37 39" src="https://github.com/Fuskus31/allocation-of-subjects/assets/70700226/a8daff69-eb43-448a-9b37-e3c3badc95f0">


To summarize, The code i have created allows us to create instances to test our functions in different cases that could be real, with the possibility of changing the number of voters and projects available with their number of places, i have coded the functions requested by my tutor to compare them and choose the one that satisfies the maximum number of students.











