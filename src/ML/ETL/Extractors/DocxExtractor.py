import docx2txt


class DocxExtractor:
    def __init__(self, docx_list: list[str] = []):
        self.files = list(filter(lambda doc: doc.endswith("docx"), docx_list))

    def _add_prefix(self, extracted: list[str]):
        for i in range(len(extracted)):
            extracted[i] = self.files[i] + " ~ " + extracted[i]
        return extracted

    def extract(self):
        extracted = list(map(docx2txt.process, self.files))
        return self._add_prefix(extracted)
