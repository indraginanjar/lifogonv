import sys

from provider.xml_file import XmlFile

class ParameterXmlFile(XmlFile):
    def get_xml_file_name(self):
        xml_file = ""

        if len(sys.argv) > 1:
            xml_file = sys.argv[1]
        
        return xml_file
