biblio = Bibliotheque("mybiblo")

# Ajout d’un livre
livre1 = Livre("1984", "George Orwell", "123456789")
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "987654321")
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)


# Ajout d’un utilisateur
util1 = Utilisateur("u1", "client1")
util2 = Utilisateur("u2", "client2")
biblio.enregistrer_utilisateur(util1)
biblio.enregistrer_utilisateur(util2)


# Emprunt
util1.emprunter_livre(biblio, "123456789") 
util2.emprunter_livre(biblio, "123456789")  


# retard
util1.livres_empruntes["123456789"] = datetime.now().replace(year=2024)
util1.retourner_livre(biblio, "123456789")

# supprimer livre
biblio.supprimer_livre("987654321")
print("\n🗑️ Livre 'Le Petit Prince' supprimé.")

# affichage
biblio.afficher_catalogue()
util1.afficher_emprunts()
util1.afficher_historique()
biblio.afficher_statistiques()

