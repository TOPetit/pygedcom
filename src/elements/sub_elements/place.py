from src.elements.sub_elements.map import GedcomMap
from ..element import GedcomElement


class GedcomPlace(GedcomElement):
    """Class representing a place element."""

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the place.

        Args:
            level (int): The level of the place.
            tag (str): The tag of the place.
            sub_elements (list): The sub elements of the place.
            value (str, optional): The value of the place. Defaults to None.

        Returns:
            GedcomPlace: The place."""
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the place. Which are location and map."""
        self.__place_infos = self.__parse_value()
        self.__map = self.__find_map()

    def __find_map(self) -> GedcomMap:
        """Find the map of the place.

        Returns:
            GedcomMap: The map of the place. None if not found.
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

        Returns:
            list: A list of locations such as city, region, country, etc...
        """
        return self.value.split(",")

    def __str__(self) -> str:
        """Return the string representation of the place.

        Returns:
            str: The string representation of the place.
        """
        return " ".join(self.__place_infos)

    def __repr__(self) -> str:
        """Return the string representation of the place.

        Returns:
            str: The string representation of the place.
        """
        return self.__str__()

    def get_data(self) -> dict:
        """Return the data of the place.

        Returns:
            dict: The data of the place.
        """
        return {
            "location": self.__place_infos,
            "map": self.__map.get_data() if self.__map is not None else None,
        }
