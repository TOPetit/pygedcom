from src.FormatException import FormatException, known_formats
from src.elements.subElements.commonEvent import GedcomCommonEvent
from src.elements.rootElements.rootElement import GedcomRootElement


class GedcomIndividual(GedcomRootElement):
    """This class represents an individual in the gedcom file.

    :param level: The level of the individual.
    :type level: int
    :param xref: The xref of the individual.
    :type xref: str
    :param tag: The tag of the individual.
    :type tag: str
    :param sub_elements: The sub elements of the individual.
    :type sub_elements: list
    :return: The individual.
    :rtype: GedcomIndividual
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the individual."""
        super().__init__(level, xref, tag, sub_elements)
        self.__name = self.__find_name()
        self.__first_name = self.__find_first_name()
        self.__last_name = self.__find_last_name()
        self.__birth = self.__init_birth()
        self.__death = self.__init_death()
        self.__sex = self.__find_sex()

    def __find_name(self):
        """Find the name of the individual.

        :return: The name of the individual.
        :rtype: str
        """
        if self.find_sub_element("NAME") != []:
            return self.find_sub_element("NAME")[0].value
        else:
            return ""

    def __find_first_name(self):
        """Find the first name of the individual.

        :return: The first name of the individual.
        :rtype: str
        """
        return self.__name.split("/")[0].split(" ")[0].strip()

    def __find_last_name(self):
        """Find the last name of the individual.

        :return: The last name of the individual.
        :rtype: str
        """
        return self.__name.split("/")[-2].strip()

    def __init_birth(self) -> GedcomCommonEvent:
        """Initialize the birth of the individual.

        :return: The birth of the individual.
        :rtype: GedcomCommonEvent
        """
        if self.find_sub_element("BIRT") != []:
            birth = self.find_sub_element("BIRT")[0]
            birth.__class__ = GedcomCommonEvent
            birth.init_properties()
            return birth
        else:
            return None

    def __init_death(self) -> GedcomCommonEvent:
        """Initialize the death of the individual.

        :return: The death of the individual.
        :rtype: GedcomCommonEvent
        """
        if self.find_sub_element("DEAT") != []:
            death = self.find_sub_element("DEAT")[0]
            death.__class__ = GedcomCommonEvent
            death.init_properties()
            return death
        else:
            return None

    def __find_sex(self):
        """Find the sex of the individual.

        :return: The sex of the individual.
        :rtype: str
        """
        return (
            self.find_sub_element("SEX")[0].value
            if self.find_sub_element("SEX") != []
            else None
        )

    def get_name(self) -> str:
        """Get the name of the individual.

        :return: The name of the individual.
        :rtype: str
        """
        return self.__name

    def get_birth(self) -> GedcomCommonEvent:
        """Get the birth of the individual.

        :return: The birth of the individual.
        :rtype: GedcomCommonEvent
        """
        return self.__birth

    def get_death(self) -> GedcomCommonEvent:
        """Get the death of the individual.

        :return: The death of the individual.
        :rtype: GedcomCommonEvent
        """
        return self.__death

    def get_first_name(self) -> str:
        """Get the first name of the individual.

        :return: The first name of the individual.
        :rtype: str
        """
        return self.__first_name

    def get_last_name(self) -> str:
        """Get the last name of the individual.

        :return: The last name of the individual.
        :rtype: str
        """
        return self.__last_name

    def __str__(self):
        """Get the string representation of the individual.

        :return: The string representation of the individual.
        :rtype: str
        """
        return self.__first_name + " " + self.__last_name

    def export(self, format="json", empty_fields=True):
        """Get the data of the individual. The result contains name, first_name, last_name, sex, birth and death.

        :param format: The format of the data.
        :type format: str
        :param empty_fields: If empty fields should be included.
        :type empty_fields: bool
        :return: The data of the individual.
        :rtype: dict
        """

        if format not in known_formats:
            raise FormatException("Format " + format + " is not supported.")

        if format == "json":
            export = {}
            if empty_fields or self.__name:
                export["name"] = self.__name
            if empty_fields or self.__first_name:
                export["first_name"] = self.__first_name
            if empty_fields or self.__last_name:
                export["last_name"] = self.__last_name
            if empty_fields or self.__sex:
                export["sex"] = self.__sex
            if empty_fields or self.__birth:
                export["birth"] = self.__birth.export() if self.__birth else ""
            if empty_fields or self.__death:
                export["death"] = self.__death.export() if self.__death else ""
        return export
