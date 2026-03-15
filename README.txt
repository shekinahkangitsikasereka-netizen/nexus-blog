Nexus Blog
Présentation

Nexus Blog est une plateforme de blog développée avec Django qui a pour objectif de partager des réflexions profondes sur la vie, la spiritualité, la psychologie humaine et la société.

Le mot “Nexus” signifie connexion ou lien.
Ce projet cherche donc à créer un lien entre les idées, les expériences humaines et les lecteurs.

À travers des articles inspirants et réfléchis, Nexus Blog encourage les visiteurs à réfléchir, apprendre et voir le monde sous un nouvel angle.

Objectifs du projet

Partager des articles inspirants et éducatifs

Créer une plateforme simple pour publier du contenu

Encourager la réflexion et la discussion

Développer une communauté de lecteurs curieux

Fonctionnalités

Publication d’articles

Page d’accueil avec les derniers articles

Page de détail pour chaque article

Système de commentaires

Tableau de bord (dashboard) pour gérer les articles

Authentification des utilisateurs (connexion / déconnexion)

Interface simple et accessible

Technologies utilisées

Le projet est développé avec les technologies suivantes :

Python

Django

HTML5

CSS3

SQLite

Git & GitHub

Installation

Pour installer et lancer le projet localement :

1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/nexus-blog.git
2. Accéder au dossier du projet
cd nexus-blog
3. Installer les dépendances
pip install -r requirements.txt
4. Appliquer les migrations
python manage.py migrate
5. Lancer le serveur
python manage.py runserver
6. Ouvrir le projet dans le navigateur
http://127.0.0.1:8000/
Structure du projet

Exemple de structure simplifiée :

nexus-blog/
│
├── manage.py
├── db.sqlite3
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── index.html
│   ├── article_detail.html...
│
├── static/
│   ├── css/
│
└── README.md
Contribution

Les contributions sont les bienvenues.

Si vous souhaitez améliorer ce projet :

Fork le projet

Créer une branche

Proposer vos modifications

Faire une Pull Request

Licence

Ce projet est open-source et peut être utilisé librement pour l'apprentissage et le développement.