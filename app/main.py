import abc
import xml.dom.minidom as minidom

from converter.xml_sourced_csv import XmlSourcedCsv
from log_4_j.event import Event as Log4JEvent
from provider.parameter_xml_file import ParameterXmlFile

def main():
    xml_file = ParameterXmlFile()
    xml_sourced_csv = XmlSourcedCsv(xml_file)
    print(xml_sourced_csv.as_string())

if __name__ == "__main__":
    main()

