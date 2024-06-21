from ..subElements.commonEvent import GedcomCommonEvent
from .rootElement import GedcomRootElement


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
        self.__export_media = self.__find_media()

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
            return GedcomCommonEvent.empty()

    def __find_husband(self) -> str:
        """Find the husband of the family.

        :return: The husband of the family.
        :rtype: str
        """
        if self.find_sub_element("HUSB") != []:
            return self.find_sub_element("HUSB")[0].get_value()
        else:
            return ""

    def __find_wife(self) -> str:
        """Find the wife of the family.

        :return: The wife of the family.
        :rtype: str
        """
        if self.find_sub_element("WIFE") != []:
            return self.find_sub_element("WIFE")[0].get_value()
        else:
            return ""

    def __find_children(self) -> list[str]:
        """Find the children of the family.

        :return: The children of the family.
        :rtype: list[str]
        """
        children = []
        for child in self.find_sub_element("CHIL"):
            children.append(child.get_value())
        return children

    def __find_are_married(self) -> str:
        """Check if the family is married.

        :return: True if the family is married, False otherwise.
        :rtype: bool
        """
        return self.find_sub_element("MARR") != [] or (
            self.find_sub_element("_UST")[0].get_value() == "MARRIED" if self.find_sub_element("_UST") != [] else False
        )

    def __find_media(self) -> list:
        """Find the media of the family.

        :return: The media of the family.
        :rtype: list
        """
        return [element.get_value() for element in self.find_sub_element("OBJE")]

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
        return [self.__export_husband, self.__export_wife]

    def get_married(self) -> bool:
        """Get if the family is married.

        :return: True if the family is married, False otherwise.
        :rtype: bool
        """
        return self.__export_married

    def get_marriage(self) -> GedcomCommonEvent:
        """Get the marriage of the family.

        :return: The marriage of the family.
        :rtype: GedcomCommonEvent
        """
        return self.__export_marriage

    def get_media(self) -> list:
        """Get the media of the family.

        :return: The media of the family.
        :rtype: list
        """
        return self.__export_media

    def set_husband(self, xref: str):
        """Set the husband of the family.

        :param xref: The xref of the husband.
        :type xref: str
        """
        self.__export_husband = xref
        husband_element = self.find_sub_element("HUSB")
        if husband_element != []:
            husband_element[0].set_value(self.__export_husband)
        else:
            self.add_sub_element(1, "HUSB", [], value=self.__export_husband)

    def set_wife(self, xref: str):
        """Set the wife of the family.

        :param xref: The xref of the wife.
        :type xref: str
        """
        self.__export_wife = xref
        wife_element = self.find_sub_element("WIFE")
        if wife_element != []:
            wife_element[0].set_value(self.__export_wife)
        else:
            self.add_sub_element(1, "WIFE", [], value=self.__export_wife)

    def set_children(self, children: list):
        """Set the children of the family.

        :param children: The xrefs of the children.
        :type children: list
        """
        self.__export_children = children
        for child in self.find_sub_element("CHIL"):
            self.remove_sub_element(child)
        for child in self.__export_children:
            self.add_sub_element(1, "CHIL", [], value=child)

    def add_child(self, child_xref: str):
        """Add a child to the family. If child already exists, do nothing.

        :param child_xref: The xref of the child to add.
        :type child_xref: str
        """
        if child_xref not in self.__export_children:
            self.__export_children.append(child_xref)
            self.add_sub_element(1, "CHIL", [], value=child_xref)

    def remove_child(self, child_xref: str):
        """Remove a child from the family. If child does not exist, do nothing.

        :param child_xref: The xref of the child to remove.
        :type child_xref: str
        """
        for child in self.find_sub_element("CHIL"):
            if child.get_value() == child_xref:
                self.remove_sub_element(child)
        self.__export_children.remove(child_xref) if child_xref in self.__export_children else None

    def remove_parent(self, parent_xref: str):
        """Remove a parent from the family. If parent does not exist, do nothing.

        :param parent_xref: The xref of the parent to remove.
        :type parent_xref: str
        """
        for parent in ["HUSB", "WIFE"]:
            if self.find_sub_element(parent) != []:
                if self.find_sub_element(parent)[0].get_value() == parent_xref:
                    self.remove_sub_element(self.find_sub_element(parent)[0])
        if self.__export_husband == parent_xref:
            self.__export_husband = ""
        if self.__export_wife == parent_xref:
            self.__export_wife = ""
