import glob
import os.path

from .Transformer import Transformer
from .Loader import Loader
from .Extractors import PdfExtractor, TxtExtractor, DocxExtractor


class ETL:
    def __init__(self, sources: list[str]):
        self.sources = sources
        self.pdfer = PdfExtractor(sources)
        self.txter = TxtExtractor(sources)
        self.docxer = DocxExtractor(sources)
        self.transformer = Transformer()
        self.loader = Loader()

    def etl(self):
        pdf_contents = self.transformer.transform(self.pdfer.extract())
        txt_contents = self.transformer.transform(self.txter.extract())
        docx_contents = self.transformer.transform(self.docxer.extract())
        self.loader.load(pdf_contents, "pdf")
        self.loader.load(txt_contents, "txt")
        self.loader.load(docx_contents, "docx")
        return self.loader.client
