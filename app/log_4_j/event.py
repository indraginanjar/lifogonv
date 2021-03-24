from xml.dom.minidom import Element

from log_4_j.location_info import LocationInfo

class Event:
    def __init__(self, logger:str, timestamp:str, level:str, thread:str, message:str, throwable_element: Element, location_info: LocationInfo) -> None:
        self._logger = logger
        self._timestamp = timestamp
        self._level = level
        self._thread = thread
        self._message = message.replace("\"", "\\\"")
        self._message = self._message.replace(",", "\\,")
        self._throwable = throwable_element
        self._location_info = location_info
    
    def get_logger(self) -> str:
        return self._logger
    
    def get_timestamp(self) -> str:
        return self._timestamp
    
    def get_level(self) -> str:
        return self._level
    
    def get_thread(self) -> str:
        return self._thread
    
    def get_message(self) -> str:
        return self._message
    
    def get_throwable(self) -> Element:
        return self._throwable
    
    def get_location_info(self) -> LocationInfo:
        return self._location_info
