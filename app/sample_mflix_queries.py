from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:kYr4xOQeonWiqZei@cluster0.vmpnj8z.mongodb.net/")
db = client["sample_mflix"]
print("conecta")

# Ejercicios de consulta
# 1- Obtener todos los títulos de las películas
# movies = db["movies"].find()
# for movie in movies:
#     print(movie["title"])

# 2- Obtener todos los títulos de las películas de género "Action"
# movies = db["movies"].find({"genres": "Action"})
# for movie in movies:
#     print(movie["title"])

# 3- Obtener todos los títulos de las películas de género "Action" que se rodaron en 2019
# movies = db["movies"].find({"genres": "Action", "year": 1914})
# for movie in movies:
#     print(movie["title"])

# 4- Obtener todos los títulos de las películas de género "Action" ordenadas por titulo
# movies = db["movies"].find({"genres": "Action"}).sort("title")
# for movie in movies:
#     print(movie["title"])

# 5- Obtener los 5 primeros los títulos de las películas de género "Action" ordenadas por titulo
# movies = db["movies"].find({"genres": "Action"}).sort("title").limit(5)
# for movie in movies:
#     print(movie["title"])

# 6- Obtener todos los títulos de las películas de género "Action" que tengan un rating de mas de 8 
movies = db["movies"].find({"genres": "Action", "imdb.rating": {"$gt": 8}})
for movie in movies:
    print(movie["title"])