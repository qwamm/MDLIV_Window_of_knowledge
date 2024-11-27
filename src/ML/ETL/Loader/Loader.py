from qdrant_client import QdrantClient


class Loader:
    def __init__(self):
        self.client = QdrantClient(":memory:")

    def load(self, raw_data: list[str], collection_name: str):
        self.client.add(
            collection_name=collection_name,
            documents=raw_data,
        )
