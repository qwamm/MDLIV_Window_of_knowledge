import glob, os
from ETL import ETL
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams
import json
from Assistant import Assistant

sources = []
for t in ("*.pdf", "*.docx", "*.txt"):
    sources.extend(glob.glob(os.path.join(os.path.dirname(__file__), t)))

client = QdrantClient(":memory:")
etl = ETL(sources, client)
etl.etl("record1")

# scroll_res = client.scroll(collection_name="record1_pdf", with_vectors=True)
# offload = {"vectors" : [], "payloads": []}
# for i in range(len(scroll_res[0])):
#     data = scroll_res[0][i]
#     offload["vectors"].append(data.vector)
#     offload["payloads"].append(data.payload)
# with open("offload.json", "w+") as file:
#     json.dump(offload, file)
#
# client = QdrantClient(":memory:")
# with open("offload.json", "r") as file:
#     data = json.load(file)
# client.create_collection("offload", vectors_config=VectorParams(size=384, distance=Distance.COSINE))
# client.upsert(
#     collection_name="offload",
#     points=[
#         PointStruct(id=i, vector=data["vectors"][i]["fast-bge-small-en"], payload=data["payloads"][i])
#         for i in range(len(data["vectors"]))
#     ]
# )
# print(client.scroll("offload", with_vectors=True))
assistant = Assistant(client)
user_request = "What programming languages are used in company?"
print(assistant.answer(user_request))

