from datetime import datetime
class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = {}   
        self.utilisateurs = {}  
        self.reservations = {}  

    def ajouter_livre(self, livre):
        self.livres[livre.isbn] = livre

    def supprimer_livre(self, isbn):
        if isbn in self.livres:
            del self.livres[isbn]

    def rechercher_livres(self, mot_cle):
        return [livre for livre in self.livres.values() if mot_cle.lower() in livre.titre.lower() or mot_cle.lower() in livre.auteur.lower()]

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.id] = utilisateur

    def emprunter_livre(self, utilisateur_id, isbn):
        utilisateur = self.utilisateurs.get(utilisateur_id)
        livre = self.livres.get(isbn)
        if utilisateur and livre:
            if livre.disponible:
                livre.emprunter()
                utilisateur.livres_empruntes[isbn] = datetime.now()
                utilisateur.historique_emprunts.append(isbn)
            else:
                print("Livre non disponible, ajout à la file de réservation.")
                self.reserver_livre(utilisateur_id, isbn)
        else:
            print("Utilisateur ou livre introuvable.")

    def retourner_livre(self, utilisateur_id, isbn):
        utilisateur = self.utilisateurs.get(utilisateur_id)
        livre = self.livres.get(isbn)
        if utilisateur and livre:
            date_emprunt = utilisateur.livres_empruntes.pop(isbn, None)
            if date_emprunt:
                livre.retourner()
                if (datetime.now() - date_emprunt).days > 15:
                    utilisateur.nb_retards += 1
                    print(f"Retour en retard ! Retards : {utilisateur.nb_retards}")
                    if utilisateur.nb_retards >= 3:
                        utilisateur.penalise = True
                        print("Utilisateur pénalisé après 3 retards.")
                self.traiter_reservations(isbn)
            else:
                print("Ce livre n'était pas emprunté par cet utilisateur.")
        else:
            print("Utilisateur ou livre introuvable.")

def reserver_livre(self, utilisateur_id, isbn):
    if isbn not in self.reservations:
        self.reservations[isbn] = [] 
    self.reservations[isbn].append(utilisateur_id)

def afficher_catalogue(self):
        for livre in self.livres.values():
            livre.afficher_info()

def afficher_statistiques(self):
    print("Statistiques simples de la bibliothèque :")

    livres = list(self.livres.values())[:3]  # prendre les 3 premiers livres ajoutés
    for livre in livres:
        print(f"{livre.titre} : {livre.nb_emprunts} emprunts")

    total_emprunts = sum(livre.nb_emprunts for livre in self.livres.values())
    print(f"Nombre total d'emprunts : {total_emprunts}")