import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="Pandasarecool2@",  
    database="movies"         
)

cursor = db.cursor()


print("-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT * FROM studio;")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT * FROM genre;")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

print("-- DISPLAYING Short Film RECORDS --")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
short_films = cursor.fetchall()
for film in short_films:
    print("Film Name: {}\nRuntime: {} minutes\n".format(film[0], film[1]))


print("-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")
directors = cursor.fetchall()
for director in directors:
    print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

db.close()