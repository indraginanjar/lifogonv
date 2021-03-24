from converter.encloser import Encloser
from log_4_j.event import Event

class EventCsvRow:
    def __init__(self, log_4_j_event: Event) -> None:
        self._event = log_4_j_event
        self._encloser = Encloser("\"")
        self._separator = ","

    def as_string(self) -> str:
        csv_row = self._encloser.enclose(self._event.get_logger())
        csv_row += self._separator + self._encloser.enclose(self._event.get_timestamp())
        csv_row += self._separator + self._encloser.enclose(self._event.get_level())
        csv_row += self._separator + self._encloser.enclose(self._event.get_thread())
        csv_row += self._separator + self._encloser.enclose(self._event.get_message())
        throwable_element = self._event.get_throwable()
        
        if throwable_element is None:
            throwable_string = 'No Throwable'
        else:
            throwable_element_cdata = throwable_element.firstChild
            
            if throwable_element_cdata is not None:
                throwable_string = throwable_element_cdata.data
        
        throwable_string = throwable_string.replace("\r\n", "\\r\\n")
        throwable_string = throwable_string.replace("\"", "\\\"")
        throwable_string = throwable_string.replace("\t", "\\\t")
        
        csv_row += self._separator + self._encloser.enclose(throwable_string)
        csv_row += self._separator + self._encloser.enclose(self._event.get_location_info().get_class())
        csv_row += self._separator + self._encloser.enclose(self._event.get_location_info().get_method())
        csv_row += self._separator + self._encloser.enclose(self._event.get_location_info().get_file())
        csv_row += self._separator + self._encloser.enclose(self._event.get_location_info().get_line())

        return csv_row
