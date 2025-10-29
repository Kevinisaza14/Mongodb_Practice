import bcrypt, re

def encriptar(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def comparar(password, hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed)

def validar_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$"
    return bool(re.match(email_pattern, email))