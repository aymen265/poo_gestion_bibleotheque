from datetime import date, timedelta, datetime

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.date_ajout = date.today()
        self.disponible = True
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
            print(f"Le livre {self.titre} déjà emprunté.")

    def retourner(self):
        if not self.disponible:
            self.disponible = True
            print(f"Le livre {self.titre} a été retourné.")
        else:
            print(f"Le livre {self.titre} est déjà disponible.")

class Utilisateur:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.livres_empruntes = {}  # ISBN → date d'emprunt
        self.historique_emprunts = []  # Liste de tuples (isbn, date_emprunt)
        self.penalise = False
        self.retards = 0

    def emprunter_livre(self, bibliotheque, isbn):
        if self.penalise:
            print("Utilisateur pénalisé.")
            return
        if len(self.livres_empruntes) >= 3:
            print("Limite d'emprunts atteinte.")
            return
        bibliotheque.emprunter_livre(self.id, isbn)

    def retourner_livre(self, bibliotheque, isbn):
        bibliotheque.retourner_livre(self.id, isbn)

    def afficher_emprunts(self):
        for isbn, date_emprunt in self.livres_empruntes.items():
            print(f"{isbn} emprunté le {date_emprunt}")

    def afficher_historique(self):
        for isbn, date_emprunt in self.historique_emprunts:
            print(f"{isbn} emprunté le {date_emprunt}")
class Reservation:
    def __init__(self, utilisateur, livre):
        self.utilisateur = utilisateur
        self.livre = livre
        self.date_reservation = datetime.now()

    def afficher_info(self):
        print(f"Réservation - Utilisateur: {self.utilisateur.nom}, Livre: {self.livre.titre}, Date: {self.date_reservation}")
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
                utilisateur.historique_emprunts.append((isbn, datetime.now()))
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
                    utilisateur.retards += 1
                    print(f"Retour en retard ! Retards : {utilisateur.retards}")
                    if utilisateur.retards >= 3:
                        utilisateur.penalise = True
                        print("Utilisateur pénalisé après 3 retards.")
                self.traiter_reservations(isbn)
            else:
                print("Ce livre n'était pas emprunté par cet utilisateur.")
        else:
            print("Utilisateur ou livre introuvable.")

    def reserver_livre(self, utilisateur_id, isbn):
        utilisateur = self.utilisateurs.get(utilisateur_id)
        livre = self.livres.get(isbn)
        if utilisateur and livre:
            reservation = Reservation(utilisateur, livre)
            if isbn not in self.reservations:
                self.reservations[isbn] = []
            self.reservations[isbn].append(reservation)
            print(f"Réservation ajoutée pour {utilisateur.nom} pour le livre '{livre.titre}'.")


    def traiter_reservations(self, isbn):
        if isbn in self.reservations and self.reservations[isbn]:
            prochaine_reservation = self.reservations[isbn].pop(0)
            print(f"Le livre '{isbn}' est maintenant disponible pour l'utilisateur {prochaine_reservation.utilisateur.nom}.")


    def afficher_catalogue(self):
        for livre in self.livres.values():
            livre.afficher_info()

    def afficher_statistiques(self):
        print("Statistiques simples de la bibliothèque :")
        livres = list(self.livres.values())[:3]
        for livre in livres:
            print(f"{livre.titre} : {livre.nb_emprunts} emprunts")
        total_emprunts = sum(livre.nb_emprunts for livre in self.livres.values())
        print(f"Nombre total d'emprunts : {total_emprunts}")


# Exemple d'utilisation :

biblio = Bibliotheque("Bibliothèque Universitaire")

# Création de livres
livre1 = Livre("1984", "George Orwell", "44444")
livre2 = Livre("L'Étranger", "Albert Camus", "33333")
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)

# Création d'utilisateurs
user1 = Utilisateur(1, "Aymen")
user2 = Utilisateur(2, "Ayoub")
user3 = Utilisateur(3, "Marouane")
user4 = Utilisateur(4, "Zakaria")
user5 = Utilisateur(5,"Zouhair")
biblio.ajouter_utilisateur(user1)
biblio.ajouter_utilisateur(user2)
biblio.ajouter_utilisateur(user3)
biblio.ajouter_utilisateur(user4)
biblio.ajouter_utilisateur(user5)
# Emprunt d'un livre par Aymen
user1.emprunter_livre(biblio, "44444")

# Tentative de réservation par Ayoub pour le même livre
user2.emprunter_livre(biblio, "44444")  # Le livre est déjà emprunté, doit déclencher une réservation

user3.emprunter_livre(biblio, "33333")
# Retour du livre par Aymen (ceci déclenche l’attribution au prochain réservé)
if "44444" in user1.livres_empruntes:
    user1.livres_empruntes["44444"] -= timedelta(days=30)
user1.retourner_livre(biblio, "44444")


user2.emprunter_livre(biblio, "44444")  # Ayoub devrait maintenant pouvoir emprunter le livre
user3.emprunter_livre(biblio, "44444")
user4.emprunter_livre(biblio, "44444")
user5.emprunter_livre(biblio, "44444")
# biblio.supprimer_livre("33333")
# print("\n🗑️ Livre 'L'Etranger' supprimé.")
# Affichage du catalogue
print("\n📚 Catalogue :")
biblio.afficher_catalogue()

# Affichage des historiques
print("\nHistorique de Aymen :")
user1.afficher_historique()
print("\nHistorique de Ayoub :")
user2.afficher_historique()
print("\nHistorique de Marouane :")
user3.afficher_historique()
print("\nRéservations actuelles :")
for reservations in biblio.reservations.values():
    for r in reservations:
        r.afficher_info() 
print("\n📊 Statistiques :")
biblio.afficher_statistiques()