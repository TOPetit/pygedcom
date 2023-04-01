from ..element import GedcomElement


# TODO: Implement the Gedcom source class.
class GedcomSource(GedcomElement):
    """The Gedcom source element.
    
    :param level: The level of the Gedcom source.
    :type level: int
    :param xref: The xref of the Gedcom source.
    :type xref: str
    :param tag: The tag of the Gedcom source.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom source.
    :type sub_elements: list
    :return: The Gedcom source.
    :rtype: GedcomSource
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom source."""
        super().__init__(level, tag, sub_elements)
        self.__xref = xref

    def get_xref(self) -> str:
        """Get the xref of the Gedcom source.

        :return: The xref of the Gedcom source.
        :rtype: str
        """
        return self.__xref

    def get_data(self):
        """Get the data of the Gedcom source.

        :return: The data of the Gedcom source.
        :rtype: dict
        """
        return {}
