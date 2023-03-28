from .element import GedcomElement


class GedcomSource(GedcomElement):
    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements)
        self.__xref = xref

    def get_xref(self) -> str:
        return self.__xref

    def get_data(self):
        return {}
