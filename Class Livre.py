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
# # new_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-3-16-148410-0")
# # new_livre.emprunter()
# # new_livre.afficher_info()
# # new_livre.emprunter()
# # new_livre.retourne()
# class Utilisateur(Livre):
#     def __init__(self,id,nom,livres_empruntes,historique_emprunts):
#         self.id = id
#         self.nom = nom
#         self.livres_empruntes = livres_empruntes # Liste de livres empruntés
#         self.historique_emprunts = historique_emprunts
#         self.penalise = False
#         super().__init__(titre=None, auteur=None, isbn=None)  # Appel du constructeur de Livre

        
            


#     def retourner_livre(self,isbn,bibliotheque):
#       deadline = timedelta(days=7)
#       if date.today()- date_emprunt > deadline:
#             self.penalise = True
#             print(f"L'utilisateur {self.nom} est pénalisé pour le livre {isbn}.")

#     def afficher_emprunts(self):



#     def afficher_hisotoire(self):


                 
       