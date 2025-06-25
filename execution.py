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
user1.retourner_livre(biblio, "44444")

user2.emprunter_livre(biblio, "44444")  # Ayoub devrait maintenant pouvoir emprunter le livre
user3.emprunter_livre(biblio, "44444")
user4.emprunter_livre(biblio, "44444")
user5.emprunter_livre(biblio, "44444")

# supprimer livre
biblio.supprimer_livre("33333")
print("\n🗑️ Livre 'Python pour les débutants' supprimé.")

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


