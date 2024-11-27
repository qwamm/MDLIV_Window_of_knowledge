import glob, os
from ETL import ETL
from Searcher import Searcher
from LLM import LLM

sources = []
for t in ("*.pdf", "*.docx", "*.txt"):
    sources.extend(glob.glob(os.path.join(os.path.dirname(__file__), t)))

etl = ETL(sources)
searcher = Searcher(etl.etl("record1"))
llm = LLM()
user_request = "What programming languages are used in our company?"
print(llm.answer(user_request, searcher.search(user_request)["match"]))
