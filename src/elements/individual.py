from src.elements.date import GedcomDate
from .element import GedcomElement


class GedcomIndividual(GedcomElement):
    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements, xref)
        # self.__name = self.find_sub_element("NAME")[0].value
        # self.__birth_infos = self.find_sub_element("BIRT")
        # if self.__birth_infos != []:
        #     self.__birth_infos = self.__birth_infos[0]
        #     if self.__birth_infos.find_sub_element("DATE") != []:
        #         self.__birth_date = GedcomDate(
        #             self.__birth_infos.find_sub_element("DATE")[0]
        #         )
