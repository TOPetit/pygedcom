from src.elements.sub_elements.date import GedcomDate
from src.elements.sub_elements.place import GedcomPlace
from ..element import GedcomElement


class GedcomCommonEvent(GedcomElement):
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
        self.__date = self.__find_date()
        self.__place = self.__find_place()

    def __find_place(self) -> GedcomPlace:
        if self.find_sub_element("PLAC") != []:
            place = self.find_sub_element("PLAC")[0]
            place.__class__ = GedcomPlace
            place.init_properties()
            return place
        else:
            return None

    def __find_date(self) -> GedcomDate:
        if self.find_sub_element("DATE") != []:
            date = self.find_sub_element("DATE")[0]
            date.__class__ = GedcomDate
            date.init_properties()
            return date
        else:
            return None

    def get_date(self) -> GedcomDate:
        return self.__date

    def get_place(self) -> GedcomPlace:
        return self.__place

    def __str__(self):
        return f"{self.__date} {self.__place}"

    def __repr__(self):
        return self.__str__()

    def get_data(self):
        return {
            "date": self.__date.get_data() if self.__date else None,
            "place": self.__place.get_data() if self.__place else None,
        }
