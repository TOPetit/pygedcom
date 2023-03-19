from .element import GedcomElement


class GedcomHead(GedcomElement):
    def __init__(self, level: int, tag: str, sub_elements: list):
        super().__init__(level, tag, sub_elements)
