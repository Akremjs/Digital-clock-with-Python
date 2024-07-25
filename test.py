import tkinter as tk
from time import strftime

class HorlogeNumerique:
    def __init__(self, root):
        self.root = root
        self.root.title("Horloge Numérique")

        # Label pour afficher l'heure
        self.label_heure = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='red')
        self.label_heure.pack(anchor='center')

        # Label pour afficher la date
        self.label_date = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='red')
        self.label_date.pack(anchor='center')

        # Label pour afficher le texte "By akrem khelifi"
        self.label_signature = tk.Label(root, text='\nBy akrem khelifi', font=('arial', 40,'bold'), fg='black', bg='red')
        self.label_signature.pack(anchor='center')

        # Appeler la méthode pour mettre à jour l'heure et la date
        self.maj_heure()

    def maj_heure(self):
        heure_actuelle = strftime('%H:%M:%S %p')
        date_actuelle = strftime('%A %d %B %Y')
        self.label_heure.config(text=heure_actuelle)
        self.label_date.config(text=date_actuelle)
        self.root.after(1000, self.maj_heure)

# Créer la fenêtre principale
root = tk.Tk()
horloge = HorlogeNumerique(root)

# Lancer la boucle principale de l'interface graphique
root.mainloop()

