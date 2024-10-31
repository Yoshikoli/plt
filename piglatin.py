class PigLatin:

    def __init__(self):
        self._cells = {}

    def set_phrase(self, cell: str, value:str) -> str:
        self._cells[cell] = value

    def get_phrase(self, cell: str, value:str) -> str:
        return self._cells.get(cell, "")

    def translate(self, cell:str, value) -> str:
        value = self.get_phrase(cell, value)
        if value == "":
            return "nil"

