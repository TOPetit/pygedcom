from .element import GedcomElement


class GedcomDate(GedcomElement):
    def __init__(self, element: GedcomElement):
        super().__init__(
            element.level, element.tag, element.get_sub_elements(), value=element.value
        )
