import abc

class XmlFile:
    @abc.abstractmethod
    def get_xml_file_name(self):
        pass

    def as_string(self):
        xml_string = "<log>"

        with open(self.get_xml_file_name()) as f:
            for line in f:
                xml_string += line

        xml_string += "</log>"
        
        return xml_string
