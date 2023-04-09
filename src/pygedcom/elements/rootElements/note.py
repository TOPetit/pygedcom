from .rootElement import GedcomRootElement

# TODO: Implement the GedcomNote class.


class GedcomNote(GedcomRootElement):
    """This class represents a note in the gedcom file.

    :param level: The level of the Gedcom note.
    :type level: int
    :param xref: The xref of the Gedcom note.
    :type xref: str
    :param tag: The tag of the Gedcom note.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom note.
    :type sub_elements: list
    :return: The Gedcom note.
    :rtype: GedcomNote
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom note."""
        super().__init__(level, xref, tag, sub_elements)
