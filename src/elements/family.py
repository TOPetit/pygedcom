from src.elements.sub_elements.date import GedcomDate
from .element import GedcomElement


class GedcomFamily(GedcomElement):
    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements)
        self.__xref = xref
        self.__husband = self.__find_husband()
        self.__wife = self.__find_wife()
        self.__children = self.__find_children()
        self.__married = self.__are_married()
        if self.__married:
            self.__marriage_date = self.__find_marriage_date()
            self.__marriage_place = self.__find_marriage_place()

    def __find_husband(self) -> str:
        if self.find_sub_element("HUSB") != []:
            return self.find_sub_element("HUSB")[0].value
        else:
            return ""

    def __find_wife(self) -> str:
        if self.find_sub_element("WIFE") != []:
            return self.find_sub_element("WIFE")[0].value
        else:
            return ""

    def __find_children(self) -> list:
        children = []
        for child in self.find_sub_element("CHIL"):
            children.append(child.value)
        return children

    def __are_married(self) -> str:
        return self.find_sub_element("MARR") != []

    def __find_marriage_date(self) -> GedcomDate:
        if self.__are_married():
            if self.find_sub_element("MARR")[0].find_sub_element("DATE") != []:
                return GedcomDate(
                    self.find_sub_element("MARR")[0].find_sub_element("DATE")[0]
                )
        return None

    def __find_marriage_place(self) -> GedcomDate:
        if self.__are_married():
            if self.find_sub_element("MARR")[0].find_sub_element("PLAC") != []:
                return GedcomDate(
                    self.find_sub_element("MARR")[0].find_sub_element("PLAC")[0]
                )
        return None

    def get_xref(self) -> str:
        return self.__xref

    def get_husband(self) -> str:
        return self.__husband

    def get_wife(self) -> str:
        return self.__wife

    def get_children(self) -> list:
        return self.__children

    def get_parents(self) -> list:
        return [self.__husband, self.__wife]

    def get_data(self):
        return {
            "husband": self.__husband,
            "wife": self.__wife,
            "children": self.__children,
            "married": self.__married,
            "marriage_date": self.__marriage_date.get_data()
            if self.__marriage_date
            else "",
            "marriage_place": self.__marriage_place.get_data()
            if self.__marriage_place
            else "",
        }
