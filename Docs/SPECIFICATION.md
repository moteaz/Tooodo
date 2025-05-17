# Spécification du Projet ToDo App

## Objectif

Créer une application ToDo permettant à l'utilisateur de gérer ses tâches quotidiennes avec un backend Django REST API et un frontend Next.js.

## Fonctionnalités principales

- Gestion des utilisateurs (inscription, authentification)
- Création, modification, suppression des tâches
- Marquer les tâches comme terminées
- Affichage des tâches filtrées (toutes, terminées, en cours)
- Interface responsive avec Next.js

## Technologies utilisées

- Backend : Django REST Framework
- Frontend : Next.js (React)
- Base de données : PostgreSQL (ou autre)
- Authentification : JWT

## Architecture

- Backend expose une API REST
- Frontend consomme l'API pour afficher et gérer les tâches
- Authentification sécurisée via JWT

## Routes principales API

| Méthode | Route            | Description             |
| ------- | ---------------- | ----------------------- |
| POST    | /api/auth/signup | Inscription utilisateur |
| POST    | /api/auth/login  | Connexion utilisateur   |
| GET     | /api/todos/      | Liste des tâches        |
| POST    | /api/todos/      | Création d'une tâche    |
| PUT     | /api/todos/:id/  | Mise à jour d'une tâche |
| DELETE  | /api/todos/:id/  | Suppression d'une tâche |

---

## Frontend

- Pages principales : login, liste des tâches, création/modification tâche
- Gestion du state via React Hooks ou Context API

---

## Déploiement

- Backend sur serveur Django (ex: Heroku, Vercel pour API)
- Frontend sur Vercel ou autre hébergeur React

---

## Tests

- Tests unitaires backend avec pytest ou unittest
- Tests frontend avec Jest/React Testing Library
