from os import path

SITE_HOST = "localhost"
SITE_PORT = 8080
DEBUG = True
SECRET_KEY = ""
with open(path.join(path.dirname(__file__), "secret.txt")) as file:
    SECRET_KEY = file.readline()
