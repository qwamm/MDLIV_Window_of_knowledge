import re


class Transformer:
    def __init__(self, content: list[str]):
        self.content = content

    def _is_symbol_ascii(self, c):
        return ord(c) in range(32, 127) or ord(c) in range(1040, 1104) or ord(c)==1105 or ord(c)==1025

    def _rm_non_ascii(self, text: str):
        return ''.join([c if self._is_symbol_ascii(c) else ' ' for c in text])

    def _rm_multy_space(self, text: str):
        return re.sub(r's+', ' ', text)

    def transform(self):
        self.content = [text.replace('\n', ' ') for text in self.content]
        self.content = list(map(self._rm_non_ascii, self.content))
        self.content = list(map(self._rm_multy_space, self.content))
        return self.content

