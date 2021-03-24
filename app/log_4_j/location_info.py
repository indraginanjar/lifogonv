class LocationInfo:
    def __init__(self, class_name: str, method: str, file: str, line: str) -> None:
        self._class = class_name
        self._method = method
        self._file = file
        self._line = line
    
    def get_class(self) -> str:
        return self._class

    def get_method(self) -> str:
        return self._method

    def get_file(self) -> str:
        return self._file

    def get_line(self) -> str:
        return self._line
