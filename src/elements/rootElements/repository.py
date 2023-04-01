from src.elements.rootElements.rootElement import GedcomRootElement

# TODO: implement the Gedcom repository element.
class GedcomRepository(GedcomRootElement):
    """This class represents a repository in the gedcom file.
    
    :param level: The level of the Gedcom repository.
    :type level: int
    :param xref: The xref of the Gedcom repository.
    :type xref: str
    :param tag: The tag of the Gedcom repository.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom repository.
    :type sub_elements: list
    :return: The Gedcom repository.
    :rtype: GedcomRepository
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom repository."""
        super().__init__(level, xref, tag, sub_elements)

    def get_data(self):
        """Get the data of the Gedcom repository. Result contains {}.

        :return: The data of the Gedcom repository.
        :rtype: dict
        """
        return {}
