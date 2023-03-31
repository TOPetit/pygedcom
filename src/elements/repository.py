from .element import GedcomElement


# TODO: implement the Gedcom repository element.
class GedcomRepository(GedcomElement):
    """The Gedcom repository element."""

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom repository.

        Args:
            level (int): The level of the Gedcom repository.
            xref (str): The xref of the Gedcom repository.
            tag (str): The tag of the Gedcom repository.
            sub_elements (list): The sub elements of the Gedcom repository.

        Returns:
            GedcomRepository: The Gedcom repository.
        """
        super().__init__(level, tag, sub_elements)
        self.__xref = xref

    def get_xref(self) -> str:
        """Get the xref of the Gedcom repository.

        Returns:
            str: The xref of the Gedcom repository.
        """
        return self.__xref

    def get_data(self):
        """Get the data of the Gedcom repository. Result contains {}.

        Returns:
            dict: The data of the Gedcom repository.
        """
        return {}
