from .element import GedcomElement


class GedcomFamily(GedcomElement):
    def __init__(self, level: int, tag: str, value: str, sub_elements: list):
        super().__init__(level, tag, value, sub_elements)