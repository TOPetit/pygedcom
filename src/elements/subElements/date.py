import re
from src.FormatException import FormatException, known_formats
from ..element import GedcomElement


class GedcomDate(GedcomElement):
    """The Gedcom date element.

    :param level: The level of the Gedcom date element.
    :type level: int
    :param tag: The tag of the Gedcom date element.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom date element.
    :type sub_elements: list
    :param value: The value of the Gedcom date element, defaults to None
    :type value: str, optional
    :return: The Gedcom date element.
    :rtype: GedcomDate
    """

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the Gedcom date element."""
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the Gedcom date element."""
        self.__parse_value()

    def __parse_value(self) -> tuple:
        """Parse the value of the Gedcom date element.

        :return: The day, month and year of the Gedcom date element.
        :rtype: tuple
        """
        if self.value.startswith("ABT"):
            self.__export_tag = "ABT"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[4:])
        elif self.value.startswith("BEF"):
            self.__export_tag = "BEF"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[4:])
        elif self.value.startswith("AFT"):
            self.__export_tag = "AFT"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[4:])
        elif self.value.startswith("CAL"):
            self.__export_tag = "CAL"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[4:])
        elif self.value.startswith("EST"):
            self.__export_tag = "EST"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[4:])
        elif self.value.startswith("INT"):
            self.__export_tag = "INT"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[4:])
        elif self.value.startswith("TO"):
            self.__export_tag = "TO"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[3:])
        elif self.value.startswith("FROM"):
            self.__export_tag = "FROM"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[5:])
        elif self.value.startswith("BET"):
            self.__export_tag = "BET"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value[4:])
            (
                self.__export_day1,
                self.__export_month1,
                self.__export_year1,
            ) = self.__parse_date(self.value.split("AND")[1][1:])
        else:
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.value)

    def __parse_date(self, date_string: str) -> tuple:
        """Parse the date string of the Gedcom date element.

        :param date_string: The date string of the Gedcom date element.
        :type date_string: str
        :return: The day, month and year of the Gedcom date element.
        :rtype: tuple
        """
        day = month = year = None
        date_string = date_string.strip()

        # Match DD MMM YYYY format
        match = re.match(r"^(\d{1,2}) ([A-Z]{3}) (\d{4})$", date_string)
        if match:
            day, month, year = match.groups()
            month = month.upper()

        # Match MMM YYYY format
        if not match:
            match = re.match(r"^([A-Z]{3}) (\d{4})$", date_string)
            if match:
                month, year = match.groups()

        # Match YYYY format
        if not match:
            match = re.match(r"^(\d{4})$", date_string)
            if match:
                (year,) = match.groups()

        return day, month, year

    def __str__(self):
        """Return the string representation of the Gedcom date element.

        :return: The string representation of the Gedcom date element.
        :rtype: str
        """
        results = [self.__export_tag] if hasattr(self, "__export_tag") else []
        if self.__export_day:
            results.append(self.__export_day)
        if self.__export_month:
            results.append(self.__export_month)
        if self.__export_year:
            results.append(self.__export_year)

        if (
            hasattr(self, "__export_day1")
            or hasattr(self, "__export_month1")
            or hasattr(self, "__export_year1")
        ):
            results.append("AND")
        if hasattr(self, "__export_day1"):
            results.append(self.__export_day1)
        if hasattr(self, "__export_month1"):
            results.append(self.__export_month1)
        if hasattr(self, "__export_year1"):
            results.append(self.__export_year1)
        return " ".join(results) if results != [] else ""

    def __repr__(self):
        """Return the string representation of the Gedcom date element.

        :return: The string representation of the Gedcom date element.
        :rtype: str
        """
        return self.__str__()
