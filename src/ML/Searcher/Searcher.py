from qdrant_client import QdrantClient


class Searcher:
    def __init__(self, qdrant_client: QdrantClient):
        self.client = qdrant_client

    def search(self, request: str):
        score = 0
        best = ''

        for col in self.client.get_collections().collections:
            response = self.client.query(
                collection_name=col.name,
                query_text=request
            )
            if response[0].score > score:
                best = response
                score = response[0].score
        return {
            "match" : best[0].document,
            "sources" : [b.document.split("~")[0][:-1:] for b in best]
        }
