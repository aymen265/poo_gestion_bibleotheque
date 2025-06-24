# 📚 Système de Gestion de Bibliothèque en Python

Ce projet est une application Python orientée objet qui permet de gérer une bibliothèque : livres, utilisateurs, emprunts, retours, réservations et statistiques.

## 🚀 Fonctionnalités principales

- Gestion des livres (ajout, suppression, affichage)
- Emprunt et retour de livres
- Limitation à 3 emprunts simultanés par utilisateur
- Détection de retards (> 15 jours)
- Pénalisation automatique après 3 retards
- File d’attente pour les réservations
- Statistiques sur les emprunts
- Historique des utilisateurs

## 🧩 Architecture du projet

Le projet est structuré autour de 4 classes principales :

- `Livre` : Représente un ouvrage
- `Utilisateur` : Représente un lecteur
- `Bibliotheque` : Gère le système entier
- `Reservation` : Gère les demandes en attente

## 🛠️ Technologies utilisées

- **Python 3.10+**
- `datetime` (module standard)
- **Git & GitHub** pour le suivi de version



