import glob
import os.path

from .Transformer import Transformer
from .Loader import Loader
from .Extractors import PdfExtractor, TxtExtractor, DocxExtractor
from qdrant_client import QdrantClient


class ETL:
    def __init__(self, sources: list[str], qdrant_client: QdrantClient):
        self.sources = sources
        self.pdfer = PdfExtractor(sources)
        self.txter = TxtExtractor(sources)
        self.docxer = DocxExtractor(sources)
        self.transformer = Transformer()
        self.loader = Loader(qdrant_client)

    def etl(self, base_collection_name: str):
        pdf_contents = self.transformer.transform(self.pdfer.extract())
        txt_contents = self.transformer.transform(self.txter.extract())
        docx_contents = self.transformer.transform(self.docxer.extract())
        self.loader.load(pdf_contents, base_collection_name + "_pdf")
        self.loader.load(txt_contents, base_collection_name + "_txt")
        self.loader.load(docx_contents, base_collection_name + "_docx")
        return self.loader.client
