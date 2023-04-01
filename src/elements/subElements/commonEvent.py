from src.FormatException import FormatException, known_formats
from src.elements.subElements.date import GedcomDate
from src.elements.subElements.place import GedcomPlace
from ..element import GedcomElement


class GedcomCommonEvent(GedcomElement):
    """Common event class. It can be a birth, death, marriage, etc... Every even with a date and a place.

    :param level: The level of the common event.
    :type level: int
    :param tag: The tag of the common event.
    :type tag: str
    :param sub_elements: The sub elements of the common event.
    :type sub_elements: list
    :param value: The value of the common event, defaults to None
    :type value: str, optional
    :return: The common event.
    :rtype: GedcomCommonEvent
    """

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the common event."""
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the common event."""
        self.__date = self.__find_date()
        self.__place = self.__find_place()

    def __find_place(self) -> GedcomPlace:
        """Find the place of the common event.

        :return: The place of the common event.
        :rtype: GedcomPlace
        """
        if self.find_sub_element("PLAC") != []:
            place = self.find_sub_element("PLAC")[0]
            place.__class__ = GedcomPlace
            place.init_properties()
            return place
        else:
            return None

    def __find_date(self) -> GedcomDate:
        """Find the date of the common event.

        :return: The date of the common event.
        :rtype: GedcomDate
        """
        if self.find_sub_element("DATE") != []:
            date = self.find_sub_element("DATE")[0]
            date.__class__ = GedcomDate
            date.init_properties()
            return date
        else:
            return None

    def get_date(self) -> GedcomDate:
        """Get the date of the common event.

        :return: The date of the common event.
        :rtype: GedcomDate
        """
        return self.__date

    def get_place(self) -> GedcomPlace:
        """Get the place of the common event.

        :return: The place of the common event.
        :rtype: GedcomPlace
        """
        return self.__place

    def __str__(self):
        """Return the string representation of the common event.

        :return: The string representation of the common event.
        :rtype: str
        """
        return f"{self.__date} {self.__place}"

    def __repr__(self):
        """Return the string representation of the common event.

        :return: The string representation of the common event.
        :rtype: str
        """
        return self.__str__()

    def export(self, format="json", empty_fields=True):
        """Get de data of the common event. Used to export the data to JSON.

        :param format: The format of the data, defaults to "json"
        :type format: str, optional
        :param empty_fields: If the empty fields should be exported, defaults to True
        :type empty_fields: bool, optional
        :return: The data of the common event.
        :rtype: dict
        """

        if format not in known_formats:
            raise FormatException("Format " + format + " is not supported.")
        if format == "json":
            export = {}
            if empty_fields or self.__date:
                export["date"] = self.__date.export() if self.__date else ""
            if empty_fields or self.__place:
                export["place"] = self.__place.export() if self.__place else ""
            return export
