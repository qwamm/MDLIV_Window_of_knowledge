

class TxtExtractor:
    def __init__(self, txt_list: list[str] = []):
        self.files = list(filter(lambda txt: txt.endswith("txt"), txt_list))

    def _open_files(self):
        return list(map(open, self.files))

    def _add_prefix(self, extracted: list[str]):
        for i in range(len(extracted)):
            extracted[i] = self.files[i] + " ~ " + extracted[i]
        return extracted

    def extract(self):
        opens = self._open_files()
        extracted = [op.read() for op in opens]
        return self._add_prefix(extracted)
