import re


class Transformer:
    def _is_symbol_ascii(self, c):
        return ord(c) in range(32, 127) or ord(c) in range(1040, 1104) or ord(c)==1105 or ord(c)==1025

    def _rm_non_ascii(self, text: str):
        return ''.join([c if self._is_symbol_ascii(c) else ' ' for c in text])

    def _rm_multy_space(self, text: str):
        return ' '.join(text.split())

    def transform(self, content: list[str] = []):
        content = [text.replace('\n', ' ') for text in content]
        content = list(map(self._rm_non_ascii, content))
        content = list(map(self._rm_multy_space, content))
        return content

