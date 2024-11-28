from qdrant_client import QdrantClient
from src.ML.LLM import LLM
from src.ML.Searcher import Searcher


# combiner class
class Assistant:
    def __init__(self, qdrant_client: QdrantClient):
        self.llm = LLM()
        self.searcher = Searcher(qdrant_client)

    def answer(self, user_request: str):
        search_results = self.searcher.search(user_request)
        llm_response = self.llm.answer(user_request, search_results["match"])
        return {
            "llm_response" : llm_response,
            "sources" : search_results["sources"]
        }
