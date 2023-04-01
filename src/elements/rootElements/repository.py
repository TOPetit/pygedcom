from src.FormatException import FormatException, known_formats
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

    def export(self, format="json", empty_fields=True):
        """Get the data of the Gedcom repository. Result contains {}.

        :param format: The format of the export.
        :type format: str
        :param empty_fields: If empty fields should be exported.
        :type empty_fields: bool
        :return: The data of the Gedcom repository.
        :rtype: dict
        """
        if format not in known_formats:
            raise FormatException("Format " + format + " is not supported.")
        if format == "json":
            export = {}

        return export
