from pypdf import PdfReader


class PdfExtractor:
    def __init__(self, pdf_list: list[str] = []):
        self.files = list(filter(lambda pdf: pdf.endswith("pdf"), pdf_list))

    def _page_extract(self, pages):
        return ''.join([page.extract_text() for page in pages])

    def _add_prefix(self, extracted: list[str]):
        for i in range(len(extracted)):
            extracted[i] = self.files[i] + " ~ " + extracted[i]
        return extracted

    def extract(self):
        pdfs = list(map(PdfReader, self.files))
        pages_lists = [pdf.pages for pdf in pdfs]
        extracted = list(map(self._page_extract, pages_lists))
        return self._add_prefix(extracted)
