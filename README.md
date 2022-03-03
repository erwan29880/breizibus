# breizibus : le brief

#### Le projet est décrit dans le cahier des charges.

#### Le projet est écrit en python, html et css sous forme de serveur web (Flask).

#### Il faut lancer le serveur avec le fichier main.py.

#### Le projet est écrit façon POO, voici les différentes classes :
- mdp.py :
  - (dé)crypte les mots de passe, vérifie si l'admninistrateur existe
- traitement.py :
  - génére un fichier texte (façon cookie) pour la gestion administrateur/utilisateur
- connexion.py :
  - connexion à la base de données Breizhibus
- connexionAdmin.py : 
  - connexion à la base de données Users
- requete.py :
  - classe héritée de la classe connexion, gère les requêtes
- admin.py :
  - classe héritée de la classe connexionAdmin.py, gère les requêtes de la partie administratives 

#### Les informations à changer pour l'utilisation de l'application : 
- dans les classes connexion.py et connexionAdmin.py:
  - l'utilisateur
  - le mot de passe
  - le port

#### fonctionnement des formulaires : 

> la gestion back-end des multiples formulaires se fait par un champs caché en front.

#### Front-end :

> utilisation d'un template Bootstrap responsive intégrant du javaScript.
