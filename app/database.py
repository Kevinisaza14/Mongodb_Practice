from pymongo import MongoClient

def connect():
        client = MongoClient("mongodb+srv://root:kYr4xOQeonWiqZei@cluster0.vmpnj8z.mongodb.net/")
        db = client["test"]
        print("Conexion a mongo DB Correcta")
        return db
    
def insertUser(db, collection, data):
    db[collection].insert_one(data)
    print("Usuario registrado con exito")

def findUsers(db, collection):
    return db[collection].find()

def find_by_email(db, collection, email):
    return db[collection].find_one({"email": email})

def delete_by_email(db, collection, email):
    return db[collection].find_one_and_delete({"email": email})

def login_by_connect(db, collection, email):
    return db[collection].find_one({"email": email})
    
def insertPurcharse(db, collection, email, data):
    result = db[collection].update_one(
        {"email": email},
        {"$push": {"compras": data}}
    )
    result = dict(result.raw_result)
    if result["updatedExisting"]:
        print("compra realizada")
    else:
        print("Usuario no encontrado en DB")

def insertPurchaseRef(db, collection, data):
    db[collection].insert_one(data)
    print("Compra realizada con exito")