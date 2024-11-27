import glob, os
from ETL import ETL
from qdrant_client import QdrantClient
from Assistant import Assistant

sources = []
for t in ("*.pdf", "*.docx", "*.txt"):
    sources.extend(glob.glob(os.path.join(os.path.dirname(__file__), t)))

client = QdrantClient(":memory:")
etl = ETL(sources, client)
etl.etl("record1")

assistant = Assistant(etl.loader.client)
user_request = "What types of health insurance are provided for employees?"
print(assistant.answer(user_request))
