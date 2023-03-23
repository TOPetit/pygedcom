from .element import GedcomElement


class GedcomObject(GedcomElement):
    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements)
        self.__xref = xref
        self.__file = self.__find_file()
        self.__format = self.__find_format()

    def __find_file(self) -> str:
        if self.find_sub_element("FILE") != []:
            return self.find_sub_element("FILE")[0].value
        else:
            return ""

    def __find_format(self) -> str:
        if self.find_sub_element("FORM") != []:
            return self.find_sub_element("FORM")[0].value
        else:
            return ""
