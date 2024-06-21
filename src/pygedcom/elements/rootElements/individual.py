from ..subElements.commonEvent import GedcomCommonEvent
from .rootElement import GedcomRootElement


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
        self.__export_name = self.__find_name()
        self.__export_first_name = self.__find_first_name()
        self.__export_last_name = self.__find_last_name()
        self.__export_birth = self.__init_birth()
        self.__export_death = self.__init_death()
        self.__export_sex = self.__find_sex()
        self.__export_media = self.__find_media()

    def __find_name(self):
        """Find the name of the individual.

        :return: The name of the individual.
        :rtype: str
        """
        if self.find_sub_element("NAME") != []:
            return self.find_sub_element("NAME")[0].get_value()
        else:
            return ""

    def __find_first_name(self):
        """Find the first name of the individual.

        :return: The first name of the individual.
        :rtype: str
        """
        return self.__export_name.split("/")[0].split(" ")[0].strip()

    def __find_last_name(self):
        """Find the last name of the individual.

        :return: The last name of the individual.
        :rtype: str
        """
        return self.__export_name.split("/")[-2].strip() if self.__export_name else ""

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
            return GedcomCommonEvent.empty()

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
            return GedcomCommonEvent.empty()

    def __find_sex(self):
        """Find the sex of the individual.

        :return: The sex of the individual.
        :rtype: str
        """
        return self.find_sub_element("SEX")[0].get_value() if self.find_sub_element("SEX") != [] else ""

    def __find_media(self) -> list:
        """Find media of the individual.

        :return: media of the individual.
        :rtype: list
        """
        return [element.get_value() for element in self.find_sub_element("OBJE")]

    def get_name(self) -> str:
        """Get the name of the individual.

        :return: The name of the individual.
        :rtype: str
        """
        return self.__export_name

    def get_birth(self) -> GedcomCommonEvent:
        """Get the birth of the individual.

        :return: The birth of the individual.
        :rtype: GedcomCommonEvent
        """
        return self.__export_birth

    def get_death(self) -> GedcomCommonEvent:
        """Get the death of the individual.

        :return: The death of the individual.
        :rtype: GedcomCommonEvent
        """
        return self.__export_death

    def get_first_name(self) -> str:
        """Get the first name of the individual.

        :return: The first name of the individual.
        :rtype: str
        """
        return self.__export_first_name

    def get_last_name(self) -> str:
        """Get the last name of the individual.

        :return: The last name of the individual.
        :rtype: str
        """
        return self.__export_last_name

    def get_sex(self) -> str:
        """Get the sex of the individual.

        :return: The sex of the individual
        :rtype: str
        """
        return self.__export_sex

    def get_media(self) -> list:
        """Get the media of the individual.

        :return: The media of the individual
        :rtype: list
        """
        return self.__export_media

    def set_first_name(self, first_name: str):
        """Set the first name of the individual.

        :param first_name: The first name of the individual.
        :type first_name: str
        """
        self.__export_first_name = first_name
        self.__export_name = f"{first_name} /{self.__export_last_name}/"
        name_element = self.find_sub_element("NAME")
        if name_element != []:
            name_element[0].set_value(self.__export_name)
        else:
            self.add_sub_element(1, "NAME", [], value=self.__export_name)

    def set_last_name(self, last_name: str):
        """Set the last name of the individual.

        :param last_name: The last name of the individual.
        :type last_name: str
        """
        self.__export_last_name = last_name
        self.__export_name = f"{self.__export_first_name} /{last_name}/"
        name_element = self.find_sub_element("NAME")
        if name_element != []:
            name_element[0].set_value(self.__export_name)
        else:
            self.add_sub_element(1, "NAME", [], value=self.__export_name)

    def set_sex(self, sex_value: str):
        """Set the sex of the individual. This is not changing family relations.

        :param sex_value: The sex value of the individual.
        :type sex_value: str
        """
        self.__export_sex = sex_value
        sex_element = self.find_sub_element("SEX")
        if sex_element != []:
            sex_element[0].set_value(self.__export_sex)
        else:
            self.add_sub_element(1, "SEX", [], value=self.__export_sex)

    def remove_family(self, family_xref: str):
        """Remove the family from the individual.

        :param family_xref: The family xref to remove.
        :type family_xref: str
        """
        for fam_tag in ["FAMC", "FAMS"]:
            for fam in self.find_sub_element(fam_tag):
                if fam.get_value() == family_xref:
                    self.remove_sub_element(fam)

    def __str__(self):
        """Get the string representation of the individual.

        :return: The string representation of the individual.
        :rtype: str
        """
        return self.__export_first_name + " " + self.__export_last_name
