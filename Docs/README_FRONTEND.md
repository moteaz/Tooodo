# Frontend - ToDo App

## Description

Frontend développé avec Next.js, consommant l'API Django REST pour afficher et gérer les tâches.

## Installation

1. Cloner le dépôt
2. Installer les dépendances :

npm install 3. Démarrer le serveur de développement :
npm run dev

## Fonctionnalités

- Interface utilisateur responsive
- Authentification utilisateur (login, logout)
- Liste des tâches avec filtres
- Création, modification, suppression des tâches

## Configuration

- Modifier le fichier `.env.local` pour indiquer l'URL de l'API backend, par exemple :

NEXT_PUBLIC_API_URL=http://localhost:8000/api

## Tests

- Utiliser Jest et React Testing Library pour les tests unitaires.

---

## Commandes utiles

- Démarrer en mode production :

npm run build
npm start
