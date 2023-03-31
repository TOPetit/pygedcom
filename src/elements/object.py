from .element import GedcomElement


class GedcomObject(GedcomElement):
    """The Gedcom object class."""

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom object.

        Args:
            level (int): The level of the Gedcom object.
            xref (str): The xref of the Gedcom object.
            tag (str): The tag of the Gedcom object.
            sub_elements (list): The sub elements of the Gedcom object.

        Returns:
            GedcomObject: The Gedcom object.
        """
        super().__init__(level, tag, sub_elements)
        self.__xref = xref
        self.__file = self.__find_file()
        self.__format = self.__find_format()

    def __find_file(self) -> str:
        """Find the file path of the Gedcom object.

        Returns:
            str: The file path of the Gedcom object.
        """
        if self.find_sub_element("FILE") != []:
            return self.find_sub_element("FILE")[0].value
        else:
            return ""

    def __find_format(self) -> str:
        """Find the format of the Gedcom object.

        Returns:
            str: The format of the Gedcom object.
        """
        if self.find_sub_element("FORM") != []:
            return self.find_sub_element("FORM")[0].value
        else:
            return ""

    def get_xref(self) -> str:
        """Get the xref of the Gedcom object.

        Returns:
            str: The xref of the Gedcom object.
        """
        return self.__xref

    def get_file(self) -> str:
        """Get the file path of the Gedcom object.

        Returns:
            str: The file path of the Gedcom object.
        """
        return self.__file

    def get_format(self) -> str:
        """Get the format of the Gedcom object.

        Returns:
            str: The format of the Gedcom object.
        """
        return self.__format

    def get_data(self):
        """Get the data of the Gedcom object.

        Returns:
            dict: The data of the Gedcom object.
        """
        return {"file": self.__file, "format": self.__format}
