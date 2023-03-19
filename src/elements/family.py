from .element import GedcomElement


class GedcomFamily(GedcomElement):
    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements, xref)
