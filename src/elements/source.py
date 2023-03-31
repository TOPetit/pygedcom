from .element import GedcomElement


# TODO: Implement the Gedcom source class.
class GedcomSource(GedcomElement):
    """The Gedcom source element."""

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom source.

        Args:
            level (int): The level of the Gedcom source.
            xref (str): The xref of the Gedcom source.
            tag (str): The tag of the Gedcom source.
            sub_elements (list): The sub elements of the Gedcom source.

        Returns:
            GedcomSource: The Gedcom source.
        """
        super().__init__(level, tag, sub_elements)
        self.__xref = xref

    def get_xref(self) -> str:
        """Get the xref of the Gedcom source.

        Returns:
            str: The xref of the Gedcom source.
        """
        return self.__xref

    def get_data(self):
        """Get the data of the Gedcom source.

        Returns:
            dict: The data of the Gedcom source.
        """
        return {}
