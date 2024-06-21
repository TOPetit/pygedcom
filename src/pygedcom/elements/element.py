class GedcomElement:
    """Class for representing a Gedcom element.

    :param level: The level of the Gedcom element.
    :type level: int
    :param tag: The tag of the Gedcom element.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom element.
    :type sub_elements: list
    :param value: The value of the Gedcom element. Defaults to None.
    :type value: str, optional
    :return: The Gedcom element.
    :rtype: GedcomElement
    """

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the Gedcom element."""
        self.__level = level
        self.__tag = tag
        self.__value = value
        self.__sub_elements = []
        if sub_elements != []:
            current_parsed_line = self.__parse_line(sub_elements[0])
            element_lines = []
            level = current_parsed_line["level"]
            for line in sub_elements[1:]:
                tmp_parsed_line = self.__parse_line(line)
                if tmp_parsed_line["level"] > level:
                    element_lines.append(line)
                else:
                    self.__sub_elements.append(
                        GedcomElement(
                            current_parsed_line["level"],
                            current_parsed_line["tag"],
                            element_lines,
                            value=current_parsed_line["value"],
                        )
                    )
                    current_parsed_line = tmp_parsed_line
                    element_lines = []
            self.__sub_elements.append(
                GedcomElement(
                    current_parsed_line["level"],
                    current_parsed_line["tag"],
                    element_lines,
                    value=current_parsed_line["value"],
                )
            )

    def __parse_line(self, line: str) -> dict:
        """Parse a line of a Gedcom file.

        :param line: The line to parse.
        :type line: str
        :return: The parsed line.
        :rtype: dict
        """
        chars = line.split(" ")
        level = int(chars.pop(0))
        xref = chars.pop(0) if chars[0].startswith("@") else None
        tag = chars.pop(0)
        value = " ".join(chars) if chars != [] else ""
        return {"level": level, "xref": xref, "tag": tag, "value": value}

    def get_sub_elements(self):
        """Get the sub elements of the Gedcom element.

        :return: The sub elements of the Gedcom element.
        :rtype: list
        """
        return self.__sub_elements

    def add_sub_element(self, level, tag, sub_elements, value=None):
        """Add a sub element to the Gedcom element.

        :param level: The level of the sub element.
        :type level: int
        :param tag: The tag of the sub element.
        :type tag: str
        :param sub_elements: The sub elements of the sub element.
        :type sub_elements: list
        :param value: The value of the sub element. Defaults to None.
        :type value: str, optional
        """
        self.__sub_elements.append(GedcomElement(level, tag, sub_elements, value))

    def remove_sub_element(self, element):
        """Remove a sub element from the Gedcom element.

        :param element: The sub element to remove.
        :type element: GedcomElement
        """
        self.__sub_elements.remove(element)

    def find_sub_element(self, tag: str) -> list:
        """Find a sub element by tag.

        :param tag: The tag of the sub element to find.
        :type tag: str
        :return: The sub element found.
        :rtype: list
        """
        return [element for element in self.__sub_elements if element.get_tag() == tag]

    def get_level(self) -> int:
        """Get the level of the Gedcom element.

        :return: The level of the Gedcom element.
        :rtype: int
        """
        return self.__level

    def get_tag(self) -> str:
        """Get the tag of the Gedcom element.

        :return: The tag of the Gedcom element.
        :rtype: str
        """
        return self.__tag

    def get_value(self) -> str:
        """Get the value of the Gedcom element.

        :return: The value of the Gedcom element.
        :rtype: str
        """
        return self.__value

    def set_value(self, value: str):
        """Set the value of the Gedcom element.

        :param value: The value to set.
        :type value: str
        """
        self.__value = value

    def __str__(self) -> str:
        """Get the string representation of the Gedcom element.

        :return: The string representation of the Gedcom element.
        :rtype: str
        """
        return "Level: " + str(self.__level) + ", Tag: " + str(self.__tag) + ", Value: " + str(self.__value)

    def __repr__(self) -> str:
        """Get the string representation of the Gedcom element.

        :return: The string representation of the Gedcom element.
        :rtype: str
        """
        return self.__str__()

    def get_gedcom(self):
        """Get the Gedcom representation of the Gedcom element.

        :return: The Gedcom representation of the Gedcom element.
        :rtype: str
        """
        gedcom = [self.get_level()]
        if hasattr(self, "get_xref") and self.get_xref():
            gedcom.append(self.get_xref())
        gedcom.append(self.get_tag())
        if self.get_value():
            gedcom.append(self.get_value())
        return f"{' '.join([str(x) for x in gedcom])}\n"

    def extract_gedcom(self) -> str:
        """Extract the Gedcom element.

        :return: The extracted Gedcom element.
        :rtype: str
        """
        return f"{self.get_gedcom()}{''.join([element.extract_gedcom() for element in self.get_sub_elements()])}"

    def export(self) -> dict:
        """Export the Gedcom element.

        :return: The exported Gedcom element.
        :rtype: dict
        """

        export_dict = {}
        prefix = f"_{self.__class__.__name__}__export_"
        for attr in dir(self):
            if attr.startswith(prefix):
                export_key = attr.replace(prefix, "")
                export_value = getattr(self, attr)
                if isinstance(export_value, GedcomElement):
                    export_dict[export_key] = export_value.export()
                else:
                    export_dict[export_key] = export_value
        return export_dict
