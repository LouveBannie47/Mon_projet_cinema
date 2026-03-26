#connection a la base de données mysql cinemadbdb en localhost avec l'utilisateur root et le mot de passe ""

import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",          # user MySQL
    password="root",   # mot de passe
    database="cinemadb"
)

print("==================== LISTE DES ACTEURS ====================")

cursor_acteur = conn.cursor()
cursor_acteur.execute("SELECT * FROM  tableacteur")

for acteur in cursor_acteur:
    print(acteur)

print("==================== LISTE DES FILMS ====================")

cursor_film = conn.cursor()
cursor_film.execute("SELECT * FROM  tablefilm")

for film in cursor_film:
    print(film)


print("==================== ACTEURS ET FILMS ====================")

cursor_jointure = conn.cursor()
cursor_jointure.execute("""
SELECT tableacteur.prenomActeur, tableacteur.nomActeur, tablefilm.titre
FROM tableacteur, tablefilm, ajouédans
WHERE tableacteur.idActeur = ajouédans.idActeur
AND ajouédans.idFilm = tablefilm.idFilm
""")

for (prenom_acteur, nom_acteur, titre_film) in cursor_jointure:
    print(prenom_acteur, nom_acteur, "a joué dans", titre_film)