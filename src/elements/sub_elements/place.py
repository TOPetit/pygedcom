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
        self.__place_infos = self.__parse_value()

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

    def __str__(self) -> str:
        return " ".join(self.__place_infos)

    def __repr__(self) -> str:
        return self.__str__()

    def get_data(self) -> dict:
        return {
            "location": self.__place_infos,
            "map": self.__map.get_data() if self.__map is not None else None,
        }
