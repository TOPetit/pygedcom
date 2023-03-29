from ..element import GedcomElement


class GedcomMap(GedcomElement):
    def __init__(self, element: GedcomElement):
        super().__init__(element.level, element.tag, element.get_sub_elements())
        self.__latitude = self.__find_latitude()
        self.__longitude = self.__find_longitude()

    def __find_latitude(self) -> float:
        latitude = self.find_sub_element("LATI")
        if latitude != []:
            return float(latitude[0].value)
        return None

    def __find_longitude(self) -> float:
        longitude = self.find_sub_element("LONG")
        if longitude != []:
            return float(longitude[0].value)
        return None

    def get_latitude(self) -> float:
        return self.__latitude

    def get_longitude(self) -> float:
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
