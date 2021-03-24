from pprint import pprint
import xml.dom.minidom as minidom
import xml.dom
from xml.dom.minidom import Element
from xml.dom.minidom import NodeList

from log_4_j.event import Event
from log_4_j.dom_location_info import DomLocationInfo

class DomEvent(Event):
    def __init__(self, dom_element: Element) -> None:
        self._dom_element = dom_element

        message_cdata = dom_element.getElementsByTagName('log4j:message')[0].firstChild
        message_cdata_string = ''

        if message_cdata is not None:
            message_cdata_string = message_cdata.data

        throwable_list = self._dom_element.getElementsByTagName('log4j:throwable')

        if len(throwable_list) == 1:
            throwable_element = throwable_list[0]
        else:
            throwable_element = dom_element.ownerDocument.createElementNS('log4j', 'throwable')

        location_info_list = self._dom_element.getElementsByTagName('log4j:locationInfo')

        if len(location_info_list) == 1:
            location_info_element = location_info_list[0]
        else:
            location_info_element = self._dom_element.ownerDocument.createElementNS('log4j', 'locationInfo')

        location_info = DomLocationInfo(location_info_element)

        Event.__init__(
                self,
                dom_element.getAttribute("logger"),
                dom_element.getAttribute("timestamp"),
                dom_element.getAttribute("level"),
                dom_element.getAttribute("thread"),
                message_cdata_string,
                throwable_element,
                location_info
            )