from src.elements.sub_elements.commonEvent import GedcomCommonEvent
from .element import GedcomElement


class GedcomIndividual(GedcomElement):
    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements)
        self.__xref = xref
        self.__name = self.find_sub_element("NAME")[0].value
        self.__birth = self.__init_birth()
        self.__death = self.__init_death()
        self.__sex = self.__find_sex()

    def __init_birth(self) -> GedcomCommonEvent:
        if self.find_sub_element("BIRT") != []:
            birth = self.find_sub_element("BIRT")[0]
            birth.__class__ = GedcomCommonEvent
            birth.init_properties()
            return birth
        else:
            return None

    def __init_death(self) -> GedcomCommonEvent:
        if self.find_sub_element("DEAT") != []:
            death = self.find_sub_element("DEAT")[0]
            death.__class__ = GedcomCommonEvent
            death.init_properties()
            return death
        else:
            return None

    def __find_sex(self):
        return (
            self.find_sub_element("SEX")[0].value
            if self.find_sub_element("SEX") != []
            else None
        )

    def get_name(self) -> str:
        return self.__name

    def get_birth(self) -> GedcomCommonEvent:
        return self.__birth

    def get_death(self) -> GedcomCommonEvent:
        return self.__death

    def get_xref(self) -> str:
        return self.__xref

    def get_first_name(self) -> str:
        return self.__name.split("/")[0].split(" ")[0].strip()

    def get_last_name(self) -> str:
        return self.__name.split("/")[-2].strip()

    def __str__(self):
        return self.get_first_name() + " " + self.get_last_name()

    def get_data(self):
        return {
            "name": self.__name,
            "first_name": self.get_first_name(),
            "last_name": self.get_last_name(),
            "sex": self.__sex,
            "birth": self.__birth.get_data() if self.__birth else "",
            "death": self.__death.get_data() if self.__death else "",
        }
