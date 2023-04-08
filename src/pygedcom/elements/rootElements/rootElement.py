from ..element import GedcomElement


class GedcomRootElement(GedcomElement):
    """Root element of the Gedcom file.

    :param level: The level of the element.
    :type level: int
    :param xref: The xref of the element.
    :type xref: str
    :param tag: The tag of the element.
    :type tag: str
    :param sub_elements: The sub elements of the element.
    :type sub_elements: list
    :return: The root element of the Gedcom file.
    :rtype: RootGedcomElement
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the rootElement."""
        super().__init__(level, tag, sub_elements)
        self.__xref = xref

    def get_xref(self) -> str:
        """Get the xref of the root element.

        :return: The xref of the root element.
        :rtype: str
        """
        return self.__xref
