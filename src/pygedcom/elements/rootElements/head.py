from .rootElement import GedcomRootElement


class GedcomHead(GedcomRootElement):
    """Class for the HEAD element.

    :param level: The level of the HEAD element.
    :type level: int
    :param tag: The tag of the HEAD element.
    :type tag: str
    :param sub_elements: The sub elements of the HEAD element.
    :type sub_elements: list
    :return: The HEAD element.
    :rtype: GedcomHead
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the HEAD element."""
        super().__init__(level, xref, tag, sub_elements)
