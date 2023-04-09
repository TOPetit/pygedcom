from .rootElement import GedcomRootElement

# TODO: Implement the submitter class.


class GedcomSubmitter(GedcomRootElement):
    """This class represents a submitter in the gedcom file.

    :param level: The level of the submitter.
    :type level: int
    :param xref: The xref of the submitter.
    :type xref: str
    :param tag: The tag of the submitter.
    :type tag: str
    :param sub_elements: The sub elements of the submitter.
    :type sub_elements: list
    :return: The submitter object.
    :rtype: GedcomSubmitter
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom submitter."""
        super().__init__(level, xref, tag, sub_elements)
