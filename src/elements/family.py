from src.elements.sub_elements.commonEvent import GedcomCommonEvent
from src.elements.sub_elements.date import GedcomDate
from src.elements.sub_elements.place import GedcomPlace
from .element import GedcomElement


class GedcomFamily(GedcomElement):
    """The family element."""

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the family.

        Args:
            level (int): The level of the family.
            xref (str): The xref of the family.
            tag (str): The tag of the family.
            sub_elements (list): The sub elements of the family.

        Returns:
            GedcomFamily: The family.
        """
        super().__init__(level, tag, sub_elements)
        self.__xref = xref
        self.__husband = self.__find_husband()
        self.__wife = self.__find_wife()
        self.__children = self.__find_children()
        self.__married = self.__find_are_married()
        if self.__married:
            self.__marriage = self.__find_marriage()

    def __find_marriage(self) -> GedcomCommonEvent:
        """Find the marriage of the family.

        Returns:
            GedcomCommonEvent: The marriage of the family.
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

        Returns:
            str: The husband of the family.
        """
        if self.find_sub_element("HUSB") != []:
            return self.find_sub_element("HUSB")[0].value
        else:
            return ""

    def __find_wife(self) -> str:
        """Find the wife of the family.

        Returns:
            str: The wife of the family.
        """
        if self.find_sub_element("WIFE") != []:
            return self.find_sub_element("WIFE")[0].value
        else:
            return ""

    def __find_children(self) -> list:
        """Find the children of the family.

        Returns:
            list: The children of the family as GedcomElements.
        """
        children = []
        for child in self.find_sub_element("CHIL"):
            children.append(child.value)
        return children

    def __find_are_married(self) -> str:
        """Check if the family is married.

        Returns:
            str: The marriage status of the family.
        """
        return self.find_sub_element("MARR") != []

    def get_xref(self) -> str:
        """Get the xref of the family.

        Returns:
            str: The xref of the family.
        """
        return self.__xref

    def get_husband(self) -> str:
        """Get the husband of the family.

        Returns:
            str: The husband of the family.
        """
        return self.__husband

    def get_wife(self) -> str:
        """Get the wife of the family.

        Returns:
            str: The wife of the family.
        """
        return self.__wife

    def get_children(self) -> list:
        """Get the children of the family.

        Returns:
            list: The children of the family.
        """
        return self.__children

    def get_parents(self) -> list:
        """Get the parents of the family.

        Returns:
            list: The parents of the family.
        """
        return [self.__husband, self.__wife]

    def get_data(self):
        """Get the data of the family. The result contains husband, wife, children, marriage status and marriage data.

        Returns:
            dict: The data of the family.
        """
        return {
            "husband": self.__husband,
            "wife": self.__wife,
            "children": self.__children,
            "married": self.__married,
            "marriage": self.__marriage.get_data() if self.__married else "",
        }
