from src.FormatException import FormatException, known_formats
from src.elements.subElements.commonEvent import GedcomCommonEvent
from src.elements.rootElements.rootElement import GedcomRootElement


class GedcomFamily(GedcomRootElement):
    """This class represents a family in the gedcom file.

    :param level: The level of the family.
    :type level: int
    :param xref: The xref of the family.
    :type xref: str
    :param tag: The tag of the family.
    :type tag: str
    :param sub_elements: The sub elements of the family.
    :type sub_elements: list
    :return: The family.
    :rtype: GedcomFamily
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the family."""
        super().__init__(level, xref, tag, sub_elements)
        self.__export_husband = self.__find_husband()
        self.__export_wife = self.__find_wife()
        self.__export_children = self.__find_children()
        self.__export_married = self.__find_are_married()
        self.__export_marriage = self.__find_marriage()

    def __find_marriage(self) -> GedcomCommonEvent:
        """Find the marriage of the family.

        :return: The marriage of the family.
        :rtype: GedcomCommonEvent
        """
        if self.find_sub_element("MARR") != []:
            marriage = self.find_sub_element("MARR")[0]
            marriage.__class__ = GedcomCommonEvent
            marriage.init_properties()
            return marriage
        else:
            return None

    def __find_husband(self) -> str:
        """Find the husband of the family.

        :return: The husband of the family.
        :rtype: str
        """
        if self.find_sub_element("HUSB") != []:
            return self.find_sub_element("HUSB")[0].value
        else:
            return ""

    def __find_wife(self) -> str:
        """Find the wife of the family.

        :return: The wife of the family.
        :rtype: str
        """
        if self.find_sub_element("WIFE") != []:
            return self.find_sub_element("WIFE")[0].value
        else:
            return ""

    def __find_children(self) -> list[str]:
        """Find the children of the family.

        :return: The children of the family.
        :rtype: list[str]
        """
        children = []
        for child in self.find_sub_element("CHIL"):
            children.append(child.value)
        return children

    def __find_are_married(self) -> str:
        """Check if the family is married.

        :return: True if the family is married, False otherwise.
        :rtype: bool
        """
        return self.find_sub_element("MARR") != []

    def get_husband(self) -> str:
        """Get the husband of the family.

        :return: The husband of the family.
        :rtype: str
        """
        return self.__export_husband

    def get_wife(self) -> str:
        """Get the wife of the family.

        :return: The wife of the family.
        :rtype: str
        """
        return self.__export_wife

    def get_children(self) -> list:
        """Get the children of the family.

        :return: The children of the family.
        :rtype: list
        """
        return self.__export_children

    def get_parents(self) -> list:
        """Get the parents of the family.

        :return: The parents of the family.
        :rtype: list
        """
        return [self.__export_husband, self.__wife]
