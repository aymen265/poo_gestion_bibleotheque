from datetime import date , timedelta
class Livre:
    def __init__(self,titre,auteur,isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.date_ajout = date.today()
        self.disponible = True # Par défaut un livre est disponible
        self.nb_emprunts = 0
    def afficher_info(self):
        disponible_text = "Disponible" if self.disponible else "Indisponible"
        print(f"Titre: {self.titre}, Auteur: {self.auteur}, ISBN: {self.isbn}, Date d'ajout: {self.date_ajout}, Disponible: {disponible_text}, Nombre d'emprunts: {self.nb_emprunts}")
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            self.nb_emprunts += 1
            print(f"Le livre {self.titre} a été emprunté.")
        else:
            print(f"Le livre {self.titre}  déja emprunté.")
    def retourne(self):
        if  self.disponible == False:
            self.disponible = True
            print(f"Le livre {self.titre} a été retourné.")
        else:
            print(f"le livre {self.titre}est dejà disponible.")


#     def afficher_hisotoire(self):


                 
       
