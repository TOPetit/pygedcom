from src.elements.sub_elements.date import GedcomDate
from src.elements.sub_elements.place import GedcomPlace
from ..element import GedcomElement


class GedcomCommonEvent(GedcomElement):
    """Common event class. It can be a birth, death, marriage, etc... Every even with a date and a place."""

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the common event.

        Args:
            level (int): The level of the common event.
            tag (str): The tag of the common event.
            sub_elements (list): The sub elements of the common event.
            value (str, optional): The value of the common event. Defaults to None.

        Returns:
            GedcomCommonEvent: The common event.
        """
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the common event."""
        self.__date = self.__find_date()
        self.__place = self.__find_place()

    def __find_place(self) -> GedcomPlace:
        """Find the place of the common event.

        Returns:
            GedcomPlace: The place of the common event.
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

        Returns:
            GedcomDate: The date of the common event."""
        if self.find_sub_element("DATE") != []:
            date = self.find_sub_element("DATE")[0]
            date.__class__ = GedcomDate
            date.init_properties()
            return date
        else:
            return None

    def get_date(self) -> GedcomDate:
        """Get the date of the common event.

        Returns:
            GedcomDate: The date of the common event.
        """
        return self.__date

    def get_place(self) -> GedcomPlace:
        """Get the place of the common event.

        Returns:
            GedcomPlace: The place of the common event.
        """
        return self.__place

    def __str__(self):
        """Return the string representation of the common event.

        Returns:
            str: The string representation of the common event.
        """
        return f"{self.__date} {self.__place}"

    def __repr__(self):
        """Return the string representation of the common event.

        Returns:
            str: The string representation of the common event.
        """
        return self.__str__()

    def get_data(self):
        """Get de data of the common event. Used to export the data to JSON."""
        return {
            "date": self.__date.get_data() if self.__date else None,
            "place": self.__place.get_data() if self.__place else None,
        }
