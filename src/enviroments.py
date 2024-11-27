import os, secrets

SITE_HOST = "localhost"
SITE_PORT = 8080
DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY", None)
if SECRET_KEY is None:
    try:
        with open("secret.txt") as f:
            SECRET_KEY = f.readline()
    except FileNotFoundError:
        with open("secret.txt", mode="w") as f:
            SECRET_KEY = secrets.token_urlsafe(16)
            f.write(SECRET_KEY)

DB_NAME = "mdliv_t1"
DB_TYPE = "postgresql"
DB_USER = 'postgres'
DB_PASSWORD = 'pgAdminPassword'
DB_PORT = 5432
DB_HOST = 'localhost'
