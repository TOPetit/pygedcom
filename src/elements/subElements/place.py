from src.FormatException import FormatException, known_formats
from src.elements.subElements.map import GedcomMap
from ..element import GedcomElement


class GedcomPlace(GedcomElement):
    """Class representing a place element.

    :param level: The level of the place.
    :type level: int
    :param tag: The tag of the place.
    :type tag: str
    :param sub_elements: The sub elements of the place.
    :type sub_elements: list
    :param value: The value of the place, defaults to None
    :type value: str, optional
    :return: The place.
    :rtype: GedcomPlace
    """

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the place."""
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the place. Which are location and map."""
        self.__place_infos = self.__parse_value()
        self.__map = self.__find_map()

    def __find_map(self) -> GedcomMap:
        """Find the map of the place.

        :return: The map of the place.
        :rtype: GedcomMap
        """
        map_elements = self.find_sub_element("MAP")
        if map_elements != []:
            map = map_elements[0]
            map.__class__ = GedcomMap
            map.init_properties()
            return map
        return None

    def __parse_value(self) -> list:
        """Parse the value of the place.

        :return: The parsed value of the place.
        :rtype: list
        """
        return self.value.split(",")

    def __str__(self) -> str:
        """Return the string representation of the place.

        :return: The string representation of the place.
        :rtype: str
        """
        return " ".join(self.__place_infos)

    def __repr__(self) -> str:
        """Return the string representation of the place.

        :return: The string representation of the place.
        :rtype: str
        """
        return self.__str__()

    def export(self, format="json", empty_fields=True) -> dict:
        """Return the data of the place.

        :param format: The format of the export, defaults to "json"
        :type format: str, optional
        :param empty_fields: If the empty fields should be exported, defaults to True
        :type empty_fields: bool, optional
        :return: The data of the place.
        :rtype: dict
        """
        if format not in known_formats:
            raise FormatException("Format " + format + " is not supported.")

        if format == "json":
            export = {}
            if empty_fields or self.__place_infos:
                export["location"] = self.__place_infos
            if empty_fields or self.__map:
                export["map"] = self.__map.export() if self.__map else ""
            return export
