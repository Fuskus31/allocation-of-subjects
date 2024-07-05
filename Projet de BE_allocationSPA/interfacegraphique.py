import tkinter as tk
from tkinter import ttk, messagebox
from main import main
import sys
import io
from spa_instance import start_instance0


class ConsoleRedirector(io.StringIO):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)





def lancer_programme():

    aleatoire_place = int(var_aleatoire_place.get())
    nbminplace = int(spin_min.get() or 1)
    nbmaxplace = int(spin_max.get() or 1)
    #print(nbminplace)
    #print(nbmaxplace)
    developpeur_or_client = int(var_dev_or_client.get())
    choix = int(var_choix.get())
    algorithme = combo_algo.get()
    main(developpeur_or_client, choix, algorithme, aleatoire_place, nbminplace, nbmaxplace)



# Création de la fenêtre principale
window = tk.Tk()
window.title("Configuration du Programme")

# Frame pour les contrôles à gauche
control_frame = ttk.Frame(window)
control_frame.pack(side=tk.LEFT, fill=tk.Y)

# Console pour les sorties à droite
text_console = tk.Text(window, height=40, width=130)
text_console.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Redirection de la sortie standard
sys.stdout = ConsoleRedirector(text_console)

# Variables pour stocker les choix de l'utilisateur
var_aleatoire_place = tk.IntVar(value=1)
var_dev_or_client = tk.IntVar(value=1)
var_choix = tk.IntVar(value=1)
var_algo = tk.StringVar(value="laisser vide en mode client")

# Widgets pour configurer aleatoire_place
label_aleatoire = tk.Label(control_frame, text="Choix aléatoire ou manuel des places  :")
label_aleatoire.pack()
radio_manuel = ttk.Radiobutton(control_frame, text="Manuel", variable=var_aleatoire_place, value=0)
radio_manuel.pack()
radio_aleatoire = ttk.Radiobutton(control_frame, text="Aléatoire", variable=var_aleatoire_place, value=1)
radio_aleatoire.pack()

# Widgets pour configurer nbminplace et nbmaxplace
label_min = tk.Label(control_frame, text="Nombre minimum de places :")
label_min.pack()
spin_min = ttk.Spinbox(control_frame, from_=0, to=100, width=5)
spin_min.pack()
label_max = tk.Label(control_frame, text="Nombre maximum de places :")
label_max.pack()
spin_max = ttk.Spinbox(control_frame, from_=1, to=100, width=5)
spin_max.pack()

# Widgets pour configurer developpeur_or_client
label_dev_or_client = tk.Label(control_frame, text="Mode (développeur, client) :")
label_dev_or_client.pack()
radio_dev = ttk.Radiobutton(control_frame, text="Développeur", variable=var_dev_or_client, value=0)
radio_dev.pack()
radio_client = ttk.Radiobutton(control_frame, text="Client", variable=var_dev_or_client, value=1)
radio_client.pack()

# Widgets pour configurer choix
label_choix = tk.Label(control_frame, text="Source des données (fichier moodle, instance générée) :")
label_choix.pack()
radio_fichier = ttk.Radiobutton(control_frame, text="Fichier Moodle", variable=var_choix, value=1)
radio_fichier.pack()
radio_instance = ttk.Radiobutton(control_frame, text="Instance Générée", variable=var_choix, value=2)
radio_instance.pack()


# Widgets pour configurer algorithme avec une Combobox
label_algo = tk.Label(control_frame, text="Algorithme (fb, hong, spa, heuristique) :")
label_algo.pack()
# Création de la Combobox avec les options disponibles
combo_algo = ttk.Combobox(control_frame, values=["fb", "hong", "spa", "heuristique"])
combo_algo.pack()

# Bouton pour lancer le programme
bouton_lancer = ttk.Button(control_frame, text="Lancer le Programme", command=lancer_programme)
bouton_lancer.pack()

def lancer_instance():
    try:
        min_choice = int(spin_minchoice.get())
        nb_personnes = int(spin_nbpersonnes.get())
        nb_project = int(spin_nbproject.get())
        start_instance0(min_choice, nb_personnes, nb_project)
        messagebox.showinfo("Instance créée", "L'instance a été créée avec succès.")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides pour les paramètres.")

# Widgets pour configurer minchoice, nbpersonnes et nbproject
label_minchoice = tk.Label(control_frame, text="Nombre minimum de choix :")
label_minchoice.pack()
spin_minchoice = ttk.Spinbox(control_frame, from_=1, to=10, width=5)
spin_minchoice.pack()

label_nbpersonnes = tk.Label(control_frame, text="Nombre de personnes :")
label_nbpersonnes.pack()
spin_nbpersonnes = ttk.Spinbox(control_frame, from_=1, to=100, width=5)
spin_nbpersonnes.pack()

label_nbproject = tk.Label(control_frame, text="Nombre de projets :")
label_nbproject.pack()
spin_nbproject = ttk.Spinbox(control_frame, from_=1, to=100, width=5)
spin_nbproject.pack()

# Bouton pour lancer l'instance
bouton_lancer_instance = ttk.Button(control_frame, text="Créer l'instance", command=lancer_instance)
bouton_lancer_instance.pack()



# Boucle principale de Tkinter
window.mainloop()

