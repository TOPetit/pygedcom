from .map import GedcomMap
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
        self.__export_place_infos = self.__parse_value()
        self.__export_map = self.__find_map()

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
        return GedcomMap.empty()

    def __parse_value(self) -> list:
        """Parse the value of the place.

        :return: The parsed value of the place.
        :rtype: list
        """
        return self.get_value().split(",") if self.get_value() != "" else []

    def get_export_place_infos(self) -> list:
        """Return the place infos.

        :return: The place infos.
        :rtype: list
        """
        return self.__export_place_infos

    def get_export_map(self) -> GedcomMap:
        """Return the map of the place.

        :return: The map of the place.
        :rtype: GedcomMap
        """
        return self.__export_map

    @classmethod
    def empty(cls):
        """Return an empty place.

        :return: An empty place.
        :rtype: GedcomPlace
        """
        return cls(0, "", [], value="")

    def __str__(self) -> str:
        """Return the string representation of the place.

        :return: The string representation of the place.
        :rtype: str
        """
        return " ".join(self.__export_place_infos)

    def __repr__(self) -> str:
        """Return the string representation of the place.

        :return: The string representation of the place.
        :rtype: str
        """
        return self.__str__()
