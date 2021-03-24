class Encloser:
    def __init__(self, encloser_string: str) -> None:
        self._encloser_string = encloser_string

    def enclose(self, value: str) -> str:
        return self._encloser_string + value + self._encloser_string
