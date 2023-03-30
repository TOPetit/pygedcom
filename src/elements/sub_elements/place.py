from src.elements.sub_elements.map import GedcomMap
from ..element import GedcomElement


class GedcomPlace(GedcomElement):
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
        (
            self.__city,
            self.__postal_code,
            self.__county,
            self.__region,
            self.__country,
        ) = self.__parse_value()[:5]
        self.__map = self.__find_map()

    def __find_map(self) -> str:
        map_elements = self.find_sub_element("MAP")
        if map_elements != []:
            map = map_elements[0]
            map.__class__ = GedcomMap
            map.init_properties()
            return map
        return None

    def __parse_value(self) -> list:
        return self.value.split(",")

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
