from pypdf import PdfReader


class PdfETL:
    def __init__(self, pdf_list: list[str]):
        self.files = pdf_list

    def _page_extract(self, pages):
        return ''.join([page.extract_text() for page in pages])

    def extract(self):
        pdfs = list(map(PdfReader, self.files))
        pages_lists = [pdf.pages for pdf in pdfs]
        return list(map(self._page_extract, pages_lists))
