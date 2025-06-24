biblio = Bibliotheque("Bibliothèque Centrale")

# Ajout d’un livre
livre1 = Livre("Python pour les débutants", "Jean Dupont", "ISBN001")
livre2 = Livre("Introduction à l’IA", "Marie Curie", "ISBN002")
livre3 = Livre("Histoire de l’informatique", "Alan Turing", "ISBN003")

biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.ajouter_livre(livre3)


# Ajout d’un utilisateur
util1 = Utilisateur("u1", "client1")
util2 = Utilisateur("u2", "client2")
biblio.ajouter_utilisateur(util1)
biblio.ajouter_utilisateur(util2)


# Emprunt
util1.emprunter_livre(biblio, "ISBN001")
util1.emprunter_livre(biblio, "ISBN002")
util1.emprunter_livre(biblio, "ISBN003") 
util1.emprunter_livre(biblio, "ISBN001")

#retourner
util1.retourner_livre(biblio, "ISBN001")

#
util2.emprunter_livre(biblio, "ISBN001")

# retard
util1.livres_empruntes["ISBN001"] = datetime.now().replace(year=2024)
util1.retourner_livre(biblio, "ISBN001")

# supprimer livre
biblio.supprimer_livre("ISBN001")
print("\n🗑️ Livre 'Python pour les débutants' supprimé.")

# affichage

print("\n📚 Catalogue :")
biblio.afficher_catalogue()

print("\n🧑‍🎓 Emprunts utilisateur :")
util1.afficher_emprunts()

print("\n📜 Historique :")
util1.afficher_historique()

print("\n📊 Statistiques :")
biblio.afficher_statistiques()

