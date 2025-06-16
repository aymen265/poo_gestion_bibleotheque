from datetime import date, timedelta      # Pour gérer les dates (emprunts, retours, délais)

class Utilisateur:
    def __init__(self, id, nom):
        self.id = id                          
        self.nom = nom                        
        self.livres_empruntes = {}            # ISBN → date d'emprunt 
        self.historique_emprunts = []         # Liste de tous les emprunts passés (y compris ceux déjà retournés)
        self.penalise = False                 # Indique si l'utilisateur est pénalisé (True/False)
        self.retards = 0                      # Nombre de retards accumulés (3 retards = pénalisation)

    def emprunter_livre(self, bibliotheque, isbn):
        if self.penalise:
            print("Utilisateur pénalisé.")     # Vérifie si l'utilisateur est bloqué
            return
        if len(self.livres_empruntes) >= 3:
            print("Limite d'emprunts atteinte.")     # L'utilisateur ne peut pas emprunter plus de 3 livres à la fois
            return
        bibliotheque.emprunter_livre(self.id, isbn)   # Délègue la gestion de l’emprunt à la bibliothèque

    def retourner_livre(self, bibliotheque, isbn):
        bibliotheque.retourner_livre(self.id, isbn)  # Délègue la gestion du retour à la bibliothèque

    def afficher_emprunts(self):
        for isbn, date_emprunt in self.livres_empruntes.items(): 
            print(f"{isbn} emprunté le {date_emprunt}")            # Affiche tous les livres actuellement empruntés

    def afficher_historique(self):
        for isbn, date_emprunt in self.historique_emprunts:
            print(f"{isbn} emprunté le {date_emprunt}")            # Affiche tout l’historique des emprunts, y compris les livres déjà rendus
