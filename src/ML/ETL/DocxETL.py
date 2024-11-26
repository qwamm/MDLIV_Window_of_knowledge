import docx2txt


class DocxETL:
    def __init__(self, docx_list: list[str]):
        self.files = docx_list

    def extract(self):
        return list(map(docx2txt.process, self.files))

