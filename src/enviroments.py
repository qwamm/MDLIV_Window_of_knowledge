import os

SITE_HOST = "localhost"
SITE_PORT = 8080
DEBUG = True
SECRET_KEY = ""
with open(os.path.join(os.path.dirname(__file__), "secret.txt")) as file:
    SECRET_KEY = file.readline()

DB_NAME = "mdliv_nuclear"
DB_TYPE = "postgresql"
DB_USER = 'postgres'
DB_PASSWORD = 'pgAdminPassword'
DB_PORT = 5432
DB_HOST = 'localhost'
