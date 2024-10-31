class PigLatin:

    def __init__(self):
        self._cells = {}

    def get_phrase(self, cell: str, value: str) -> str:
        return self._cells.get(cell, "")

    def translate(self) -> str:
        pass
