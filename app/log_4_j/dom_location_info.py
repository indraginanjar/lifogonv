from xml.dom.minidom import Element

from log_4_j.location_info import LocationInfo

class DomLocationInfo(LocationInfo):
    def __init__(self, dom_element: Element) -> None:
        LocationInfo.__init__(
                self,
                dom_element.getAttribute("class"),
                dom_element.getAttribute("method"),
                dom_element.getAttribute("file"),
                dom_element.getAttribute("line"),
            )
