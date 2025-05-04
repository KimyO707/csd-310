import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="Pandasarecool2@",  
    database="movies"
)

cursor = db.cursor()

def show_films(cursor, title):
    query = """
    SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()

    print("\n-- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")


cursor.execute("""
INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
VALUES ('Five Nights at Freddy''s', '2023', '109', 'Emma Tammi', 2, 1);
""")

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


cursor.execute("""
UPDATE film
SET genre_id = 1
WHERE film_name = 'Alien';
""")

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")


cursor.execute("""
DELETE FROM film
WHERE film_name = 'Gladiator';
""")

show_films(cursor, "DISPLAYING FILMS AFTER DELETE - Removed Gladiator")

db.commit()
db.close()