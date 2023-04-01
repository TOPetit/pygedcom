from src.FormatException import FormatException, known_formats
from ..element import GedcomElement


class GedcomMap(GedcomElement):
    """Class representing a Gedcom map element.

    :param level: The level of the Gedcom map element.
    :type level: int
    :param tag: The tag of the Gedcom map element.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom map element.
    :type sub_elements: list
    :param value: The value of the Gedcom map element, defaults to None
    :type value: str, optional
    :return: The Gedcom map element.
    :rtype: GedcomMap
    """

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the Gedcom map element."""
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the Gedcom map element."""
        self.__latitude = self.__find_latitude()
        self.__longitude = self.__find_longitude()

    def __find_latitude(self) -> str:
        """Find the latitude of the Gedcom map element.

        :return: The latitude of the Gedcom map element.
        :rtype: str
        """
        latitude = self.find_sub_element("LATI")
        if latitude != []:
            return latitude[0].value
        return None

    def __find_longitude(self) -> str:
        """Find the longitude of the Gedcom map element.

        :return: The longitude of the Gedcom map element.
        :rtype: str
        """
        longitude = self.find_sub_element("LONG")
        if longitude != []:
            return longitude[0].value
        return None

    def get_latitude(self) -> str:
        """Get the latitude of the Gedcom map element.

        :return: The latitude of the Gedcom map element.
        :rtype: str
        """
        return self.__latitude

    def get_longitude(self) -> str:
        """Get the longitude of the Gedcom map element.

        :return: The longitude of the Gedcom map element.
        :rtype: str
        """
        return self.__longitude

    def __str__(self) -> str:
        """Get the string representation of the Gedcom map element.

        :return: The string representation of the Gedcom map element.
        :rtype: str
        """
        return f"Map: {self.__latitude}, {self.__longitude}"

    def __repr__(self) -> str:
        """Get the string representation of the Gedcom map element.

        :return: The string representation of the Gedcom map element.
        :rtype: str
        """
        return self.__str__()

    def export(self, format="json", empty_fields=True) -> dict:
        """Get the data of the Gedcom map element. The result contains the latitude and longitude.

        :param format: The format of the export, defaults to "json"
        :type format: str, optional
        :param empty_fields: If True, the empty fields are exported, defaults to True
        :type empty_fields: bool, optional
        :return: The data of the Gedcom map element.
        :rtype: dict
        """

        if format not in known_formats:
            raise FormatException("Format " + format + " is not supported.")

        if format == "json":
            export = {}
            if empty_fields or self.__latitude:
                export["latitude"] = self.__latitude
            if empty_fields or self.__longitude:
                export["longitude"] = self.__longitude
            return export
