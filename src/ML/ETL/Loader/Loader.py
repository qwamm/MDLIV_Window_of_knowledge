from qdrant_client import QdrantClient


class Loader:
    def __init__(self):
        self.client = QdrantClient(":memory:")
        self.collection_name = "collection_0"

    def load(self, raw_data: list[str]):
        self.client.add(
            collection_name=self.collection_name,
            documents=raw_data,
        )
        self.collection_name = "collection_" + self.collection_name[-1]

# pdfs = glob.glob(os.path.join(os.path.dirname(__file__), "*.pdf"))
# pdfer = PdfExtractor(["Overview.pdf", "AI.pdf", "Cloud.pdf"])
# tr = Transformer(pdfer.extract())
#
#
#
# print(loader.client.query(
#     collection_name="pdfs",
#     query_text="What are main points of ai services?"))
