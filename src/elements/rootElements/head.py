from ..element import GedcomElement


class GedcomHead(GedcomElement):
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

    def __init__(self, level: int, tag: str, sub_elements: list):
        """Initialize the HEAD element."""
        super().__init__(level, tag, sub_elements)
