from .rootElement import GedcomRootElement


class GedcomObject(GedcomRootElement):
    """This class represents an object in the gedcom file.

    :param level: The level of the Gedcom object.
    :type level: int
    :param xref: The xref of the Gedcom object.
    :type xref: str
    :param tag: The tag of the Gedcom object.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom object.
    :type sub_elements: list
    :return: The Gedcom object.
    :rtype: GedcomObject
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom object."""
        super().__init__(level, xref, tag, sub_elements)
        self.__export_file = self.__find_file()
        self.__export_format = self.__find_format()

    def __find_file(self) -> str:
        """Find the file path of the Gedcom object.

        :return: The file path of the Gedcom object.
        :rtype: str
        """
        if self.find_sub_element("FILE") != []:
            return self.find_sub_element("FILE")[0].get_value()
        else:
            return ""

    def __find_format(self) -> str:
        """Find the format of the Gedcom object.

        :return: The format of the Gedcom object.
        :rtype: str
        """
        if self.find_sub_element("FORM") != []:
            return self.find_sub_element("FORM")[0].get_value()
        else:
            return ""

    def get_file(self) -> str:
        """Get the file path of the Gedcom object.

        :return: The file path of the Gedcom object.
        :rtype: str
        """
        return self.__export_file

    def get_format(self) -> str:
        """Get the format of the Gedcom object.

        :return: The format of the Gedcom object.
        :rtype: str
        """
        return self.__export_format
