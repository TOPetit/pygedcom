from ..element import GedcomElement


class GedcomMap(GedcomElement):
    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        self.__latitude = self.__find_latitude()
        self.__longitude = self.__find_longitude()

    def __find_latitude(self) -> str:
        latitude = self.find_sub_element("LATI")
        if latitude != []:
            return latitude[0].value
        return None

    def __find_longitude(self) -> str:
        longitude = self.find_sub_element("LONG")
        if longitude != []:
            return longitude[0].value
        return None

    def get_latitude(self) -> str:
        return self.__latitude

    def get_longitude(self) -> str:
        return self.__longitude

    def __str__(self) -> str:
        return f"Map: {self.__latitude}, {self.__longitude}"

    def __repr__(self) -> str:
        return self.__str__()

    def get_data(self) -> dict:
        return {
            "latitude": self.__latitude,
            "longitude": self.__longitude,
        }
