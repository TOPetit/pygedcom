from .date import GedcomDate
from .place import GedcomPlace
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
        self.__export_date = self.__find_date()
        self.__export_place = self.__find_place()
        self.__export_media = self.__find_media()

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
            return GedcomPlace.empty()

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
            return GedcomDate.empty()

    def __find_media(self) -> list:
        """Find the media of the common event.

        :return: The media of the common event.
        :rtype: list
        """
        return [element.get_value() for element in self.find_sub_element("OBJE")]

    def get_date(self) -> GedcomDate:
        """Get the date of the common event.

        :return: The date of the common event.
        :rtype: GedcomDate
        """
        return self.__export_date

    def get_place(self) -> GedcomPlace:
        """Get the place of the common event.

        :return: The place of the common event.
        :rtype: GedcomPlace
        """
        return self.__export_place

    def get_media(self) -> list:
        """Get the media of the common event.

        :return: The media of the common event.
        :rtype: list
        """
        return self.__export_media

    @classmethod
    def empty(cls):
        """Return an empty common event.

        :return: An empty common event.
        :rtype: GedcomCommonEvent
        """
        return cls(0, "", [])

    def __str__(self):
        """Return the string representation of the common event.

        :return: The string representation of the common event.
        :rtype: str
        """
        return f"{self.__export_date} {self.__export_place}"

    def __repr__(self):
        """Return the string representation of the common event.

        :return: The string representation of the common event.
        :rtype: str
        """
        return self.__str__()
