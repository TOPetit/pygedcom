import re
from ..element import GedcomElement


class GedcomDate(GedcomElement):
    """The Gedcom date element."""

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the Gedcom date element.

        Args:
            level (int): The level of the Gedcom date element.
            tag (str): The tag of the Gedcom date element.
            sub_elements (list): The sub elements of the Gedcom date element.
            value (str, optional): The value of the Gedcom date element. Defaults to None.

        Returns:
            GedcomDate: The Gedcom date element.
        """
        super().__init__(level, tag, sub_elements, value=value)
        self.init_properties()

    def init_properties(self):
        """Initialize the properties of the Gedcom date element."""
        self.__day, self.__month, self.__year = self.__parse_value()

    def __parse_value(self) -> tuple:
        """Parse the value of the Gedcom date element.

        Returns:
            tuple: The day, month and year of the Gedcom date element.
        """
        if self.value == "":
            return None, None, None
        if self.value.startswith("ABT"):
            return self.__parse_date(self.value[4:])
        if self.value.startswith("BEF"):
            return self.__parse_date(self.value[4:])
        if self.value.startswith("AFT"):
            return self.__parse_date(self.value[4:])
        if self.value.startswith("CAL"):
            return self.__parse_date(self.value[4:])
        if self.value.startswith("EST"):
            return self.__parse_date(self.value[4:])
        if self.value.startswith("INT"):
            return self.__parse_date(self.value[4:])
        if self.value.startswith("TO"):
            return self.__parse_date(self.value[3:])
        if self.value.startswith("FROM"):
            # TODO Implement 2 dates format
            return None, None, None
        if self.value.startswith("BET"):
            # TODO Implement 2 dates format
            return None, None, None
        # TODO Implement 2 dates format with OR
        else:
            return self.__parse_date(self.value)

    def __parse_date(self, date_string: str) -> tuple:
        """Parse the date string of the Gedcom date element.

        Args:
            date_string (str): The date string of the Gedcom date element.

        Returns:
            tuple: The day, month and year of the Gedcom date element.
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

        Returns:
            str: The string representation of the Gedcom date element.
        """
        results = []
        if self.__day:
            results.append(self.__day)
        if self.__month:
            results.append(self.__month)
        if self.__year:
            results.append(self.__year)
        return " ".join(results) if results != [] else ""

    def __repr__(self):
        """Return the string representation of the Gedcom date element.

        Returns:
            str: The string representation of the Gedcom date element.
        """
        return self.__str__()

    def get_data(self) -> dict:
        """Return the data of the Gedcom date element. The result contains the day, month and year of the Gedcom date element.

        Returns:
            dict: The data of the Gedcom date element.
        """
        return {
            "day": self.__day,
            "month": self.__month,
            "year": self.__year,
        }
