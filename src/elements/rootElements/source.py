from src.elements.rootElements.rootElement import GedcomRootElement


# TODO: Implement the Gedcom source class.
class GedcomSource(GedcomRootElement):
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
        super().__init__(level, xref, tag, sub_elements)

    def export(self):
        """Get the data of the Gedcom source.

        :return: The data of the Gedcom source.
        :rtype: dict
        """
        return {}
