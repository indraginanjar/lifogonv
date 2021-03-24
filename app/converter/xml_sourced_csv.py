from xml.dom import expatbuilder

from log_4_j.dom_event import DomEvent
from log_4_j.event import Event
from log_4_j.event_csv_row import EventCsvRow
from provider.xml_file import XmlFile


class XmlSourcedCsv:
    def __init__(self, xml_file: XmlFile) -> None:
        self._xml_file = xml_file
    
    def get_column_heads(self):
        return '"#", "logger", "timestamp", "level", "thread", "messages", "throwable", "class", "method", "file", "line"'

    def as_string(self) -> str:
        xml_string = self._xml_file.as_string()
        document = expatbuilder.parseString(xml_string, False)
        events = document.getElementsByTagName('log4j:event')
        csv = self.get_column_heads()
        row_num = 0

        for ev in events:
            row_num += 1
            csv += "\n\"" + str(row_num) + "\"" + ", "
            event = DomEvent(ev)
            event_csv_row = EventCsvRow(event)
            row_string = event_csv_row.as_string()
            csv += row_string

        return csv
