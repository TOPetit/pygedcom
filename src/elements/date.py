from .element import GedcomElement


class GedcomDate:
    months = [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
    ]
    date_tags = ["ABT", "AFT", "BEF", "CAL", "EST", "INT"]

    def __init__(self, element: GedcomElement):
        self.__value = element.value
        split = self.__value.split(" ")
        self.__year = None
        self.__month = None
        self.__day = None
        self.__tag = None
        if len(split) == 1:
            # Only year
            self.__year = int(split[0])
        elif len(split) == 2:
            if split[0] in self.months:
                # MONTH YEAR
                self.__month = split[0]
                self.__year = int(split[1])
            else:
                # TAG YEAR
                self.__tag = split[0]
                self.__year = int(split[1])
        elif len(split) == 3:
            if split[0] in self.date_tags:
                # TAG MONTH YEAR
                self.__tag = split[0]
                self.__month = split[1]
                self.__year = int(split[2])
            else:
                # DAY MONTH YEAR
                self.__day = int(split[0])
                self.__month = split[1]
                self.__year = int(split[2])
        elif len(split) == 4:
            # TAG DAY MONTH YEAR
            self.__tag = split[0]
            self.__day = int(split[1])
            self.__month = split[2]
            self.__year = int(split[3])

    def get_year(self) -> int:
        return self.__year

    def get_day(self) -> int:
        return self.__day

    def get_month(self) -> int:
        return self.__month

    def get_tag(self) -> str:
        return self.__tag

    def __str__(self):
        result = []
        if self.__day:
            result.append(str(self.__day))
        if self.__month:
            result.append(self.__month)
        if self.__year:
            result.append(str(self.__year))
        return " ".join(result)
