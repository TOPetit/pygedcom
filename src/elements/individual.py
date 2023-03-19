from src.elements.date import GedcomDate
from .element import GedcomElement


class GedcomIndividual(GedcomElement):
    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements)
        self.__xref = xref
        self.__name = self.find_sub_element("NAME")[0].value
        self.__date_of_birth = self.__find_date_of_birth()
        self.__date_of_death = self.__find_date_of_death()

    def __find_date_of_death(self) -> GedcomDate:
        if (
            self.find_sub_element("DEAT") != []
            and self.find_sub_element("DEAT")[0].find_sub_element("DATE") != []
        ):
            return GedcomDate(
                self.find_sub_element("DEAT")[0].find_sub_element("DATE")[0]
            )
        else:
            return None

    def __find_date_of_birth(self) -> GedcomDate:
        if (
            self.find_sub_element("BIRT") != []
            and self.find_sub_element("BIRT")[0].find_sub_element("DATE") != []
        ):
            return GedcomDate(
                self.find_sub_element("BIRT")[0].find_sub_element("DATE")[0]
            )
        else:
            return None

    def get_name(self) -> str:
        return self.__name

    def get_date_of_birth(self) -> GedcomDate:
        return self.__date_of_birth

    def get_date_of_death(self) -> GedcomDate:
        return self.__date_of_death
