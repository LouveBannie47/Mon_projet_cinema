# Cinema DB Python

Projet de gestion de films et d'acteurs avec Python et MySQL. Ce projet permet d’afficher la liste des acteurs, des films, ainsi que les relations entre eux (quel acteur a joué dans quel film).

## Contenu

- `mysql_ionis_cinema.py` : fichier principal avec les requêtes SQL
- `cinemadb.sql` : export de la base de données MySQL
- `README.md` : ce fichier

## Prérequis

- Python 3.10
- MySQL
- mysql-connector-python (`pip install mysql-connector-python`)


## Installation et exécution
- Importer la base de données dans MySQL : `mysql -u root -p < cinemadb.sql`
- Exécuter le programme : `python mysql_ionis_cinema.py`

## Fonctionnalités
- Affiche la liste de tous les acteurs
- Affiche la liste de tous les films
- Affiche quel acteur a joué dans quel film grâce à la table de jointure ajouédans

## Base de données

<img width="1916" height="1003" alt="Capture d&#39;écran 2026-03-26 142310" src="https://github.com/user-attachments/assets/e0cc0c35-8633-4fae-8736-301ef84c438b" />

## Exemple de sortie

==================== LISTE DES ACTEURS ====================

(1, 'DiCaprio', 'Leonardo', 'Américaine')

(2, 'Johansson', 'Scarlett', 'Américaine')

==================== LISTE DES FILMS ====================

(1, 'Inception', '2010', 'Science-fiction', 148, 'Christopher Nolan')

(2, 'Lucy', '2014', 'Action', 89, 'Luc Besson')

==================== ACTEURS ET FILMS ====================

Leonardo DiCaprio a joué dans Inception

Scarlett Johansson a joué dans Lucy



