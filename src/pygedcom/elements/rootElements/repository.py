from .rootElement import GedcomRootElement


class GedcomRepository(GedcomRootElement):
    """This class represents a repository in the gedcom file.

    :param level: The level of the Gedcom repository.
    :type level: int
    :param xref: The xref of the Gedcom repository.
    :type xref: str
    :param tag: The tag of the Gedcom repository.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom repository.
    :type sub_elements: list
    :return: The Gedcom repository.
    :rtype: GedcomRepository
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom repository."""
        super().__init__(level, xref, tag, sub_elements)
        self.__export_name = self.__find_name()

    def __find_name(self) -> str:
        """Find the name of the repository.

        :return: The name of the repository.
        :rtype: str
        """
        name = self.find_sub_element("NAME")
        if name != []:
            return name[0].get_value()
        return ""

    def get_name(self) -> str:
        """Get the name of the repository.

        :return: The name of the repository.
        :rtype: str
        """
        return self.__export_name

    def __str__(self) -> str:
        """Get the string representation of the repository.

        :return: The string representation of the repository.
        :rtype: str
        """
        return f"Repository: {self.__export_name}"
