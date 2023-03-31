from ..element import GedcomElement


class GedcomMap(GedcomElement):
    """Class representing a Gedcom map element."""

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the Gedcom map element.

        Args:
            level (int): The level of the Gedcom map element.
            tag (str): The tag of the Gedcom map element.
            sub_elements (list): The sub elements of the Gedcom map element.
            value (str, optional): The value of the Gedcom map element. Defaults to None.

        Returns:
            GedcomMap: The Gedcom map element.
        """
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the Gedcom map element."""
        self.__latitude = self.__find_latitude()
        self.__longitude = self.__find_longitude()

    def __find_latitude(self) -> str:
        """Find the latitude of the Gedcom map element.

        Returns:
            str: The latitude of the Gedcom map element.
        """
        latitude = self.find_sub_element("LATI")
        if latitude != []:
            return latitude[0].value
        return None

    def __find_longitude(self) -> str:
        """Find the longitude of the Gedcom map element.

        Returns:
            str: The longitude of the Gedcom map element.
        """
        longitude = self.find_sub_element("LONG")
        if longitude != []:
            return longitude[0].value
        return None

    def get_latitude(self) -> str:
        """Get the latitude of the Gedcom map element.

        Returns:
            str: The latitude of the Gedcom map element.
        """
        return self.__latitude

    def get_longitude(self) -> str:
        """Get the longitude of the Gedcom map element.

        Returns:
            str: The longitude of the Gedcom map element.
        """
        return self.__longitude

    def __str__(self) -> str:
        """Get the string representation of the Gedcom map element.

        Returns:
            str: The string representation of the Gedcom map element."""
        return f"Map: {self.__latitude}, {self.__longitude}"

    def __repr__(self) -> str:
        """Get the string representation of the Gedcom map element.

        Returns:
            str: The string representation of the Gedcom map element.
        """
        return self.__str__()

    def get_data(self) -> dict:
        """Get the data of the Gedcom map element. The result contains the latitude and longitude.

        Returns:
            dict: The data of the Gedcom map element.
        """
        return {
            "latitude": self.__latitude,
            "longitude": self.__longitude,
        }
