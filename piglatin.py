from glob import translate


class PigLatin:
    def __init__(self):
        self._phases = {}
        self._translate = set()

    def set_phrase(self, phase: str, value:str) -> str:
        self._phases[phase] = value

    def get(self, phase: str):
        return self._phases.get(phase, "")

    def translate(self, phase:str) -> str:
        value = self.get(phase)
        if value == "hello world":
            result = "hello world"
        if value == "":
            result = "nil"
        if value.endswith("y"):
            result = phase + "nay"
        elif value.endswith("a") or phase.endswith("e") or phase.endswith("i") or phase.endswith("o") or phase.endswith("u"):
            result = phase + "yay"
        return result

