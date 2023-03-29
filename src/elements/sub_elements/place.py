from src.elements.sub_elements.map import GedcomMap
from ..element import GedcomElement


class GedcomPlace(GedcomElement):
    def __init__(self, element: GedcomElement):
        super().__init__(element.level, element.tag, element.get_sub_elements())
        self.__value = element.value
        (
            self.__city,
            self.__postal_code,
            self.__county,
            self.__region,
            self.__country,
        ) = self.__parse_value()
        self.__map = self.__find_map()

    def __find_map(self) -> str:
        map_elements = self.find_sub_element("MAP")
        if map_elements != []:
            return GedcomMap(map_elements[0])
        return None

    def __parse_value(self) -> list:
        return self.__value.split(",")

    def get_city(self) -> str:
        return self.__city

    def get_postal_code(self) -> str:
        return self.__postal_code

    def get_county(self) -> str:
        return self.__county

    def get_region(self) -> str:
        return self.__region

    def get_country(self) -> str:
        return self.__country

    def get_value(self) -> str:
        return self.__value

    def __str__(self) -> str:
        return self.__city + ", " + self.__postal_code + self.__country

    def __repr__(self) -> str:
        return self.__str__()

    def get_data(self) -> dict:
        return {
            "city": self.__city,
            "postal_code": self.__postal_code,
            "county": self.__county,
            "region": self.__region,
            "country": self.__country,
            "map": self.__map.get_data() if self.__map is not None else None,
        }
