

class TxtExtractor:
    def __init__(self, txt_list: list[str]):
        self.files = txt_list

    def _open_files(self):
        return list(map(open, self.files))

    def extract(self):
        opens = self._open_files()
        return [op.read() for op in opens]
