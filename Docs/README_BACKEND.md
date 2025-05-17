# Backend - ToDo App

## Description

Backend développé avec Django REST Framework fournissant une API REST sécurisée pour la gestion des tâches.

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel
3. Installer les dépendances :

pip install -r requirements.txt

4. Configurer la base de données dans `settings.py`
5. Appliquer les migrations :

python manage.py migrate

6. Lancer le serveur :

python manage.py runserver

## Points importants

- Authentification JWT configurée
- Endpoints sécurisés via permissions Django REST
- Tests backend disponibles dans `/tests`

## Utilisation

Utiliser les endpoints API pour créer, modifier, supprimer et récupérer les tâches.

---

## Commandes utiles

- Lancer les tests :

python manage.py test

- Créer un superutilisateur :
