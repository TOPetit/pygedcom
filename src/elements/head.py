from .element import GedcomElement


class GedcomHead(GedcomElement):
    """Class for the HEAD element."""

    def __init__(self, level: int, tag: str, sub_elements: list):
        """Initialize the HEAD element.

        Args:
            level (int): The level of the HEAD element.
            tag (str): The tag of the HEAD element.
            sub_elements (list): The sub elements of the HEAD element.

        Returns:
            GedcomHead: The HEAD element.
        """
        super().__init__(level, tag, sub_elements)
