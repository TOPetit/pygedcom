from src.elements.rootElements.rootElement import GedcomRootElement
from src.FormatException import FormatException, known_formats


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

    def export(self, format="json", empty_fields=True) -> dict:
        """Export the HEAD element.

        :param format: The format of the export.
        :type format: str
        :param empty_fields: If empty fields should be exported.
        :type empty_fields: bool
        :return: The exported HEAD element.
        :rtype: dict
        """
        if format not in known_formats:
            raise FormatException("Format " + format + " is not supported.")
        return {}
