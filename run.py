import uvicorn
from src import SITE_PORT, SITE_HOST, DEBUG

if __name__ == "__main__":
    uvicorn.run("src.main:app", host=SITE_HOST, port=SITE_PORT, reload=DEBUG)
