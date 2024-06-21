import re
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

    def __parse_value(self):
        """Parse the value of the Gedcom date element. This function initializes the following properties:

        - __export_tag
        - __export_day
        - __export_month
        - __export_year

        and if needed (when the format contains 2 dates):

        - __export_day1
        - __export_month1
        - __export_year1
        """
        if self.get_value().startswith("ABT"):
            self.__export_tag = "ABT"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[4:])
        elif self.get_value().startswith("BEF"):
            self.__export_tag = "BEF"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[4:])
        elif self.get_value().startswith("AFT"):
            self.__export_tag = "AFT"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[4:])
        elif self.get_value().startswith("CAL"):
            self.__export_tag = "CAL"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[4:])
        elif self.get_value().startswith("EST"):
            self.__export_tag = "EST"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[4:])
        elif self.get_value().startswith("INT"):
            self.__export_tag = "INT"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[4:])
        elif self.get_value().startswith("TO"):
            self.__export_tag = "TO"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[3:])
        elif self.get_value().startswith("FROM"):
            self.__export_tag = "FROM"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[5:])
        elif self.get_value().startswith("BET"):
            self.__export_tag = "BET"
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value()[4:])
            (
                self.__export_day1,
                self.__export_month1,
                self.__export_year1,
            ) = self.__parse_date(self.get_value().split("AND")[1][1:])
        else:
            (
                self.__export_day,
                self.__export_month,
                self.__export_year,
            ) = self.__parse_date(self.get_value())

    def __parse_date(self, date_string: str) -> tuple:
        """Parse the date string of the Gedcom date element.

        :param date_string: The date string of the Gedcom date element.
        :type date_string: str
        :return: The day, month and year of the Gedcom date element.
        :rtype: tuple
        """
        day = month = year = ""
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

    @classmethod
    def empty(cls):
        """Return an empty Gedcom date element.

        :return: An empty Gedcom date element.
        :rtype: GedcomDate
        """
        return cls(0, "", [], value="")

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

        if hasattr(self, "__export_day1") or hasattr(self, "__export_month1") or hasattr(self, "__export_year1"):
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
