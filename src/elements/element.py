# TODO: make the parameters private


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
        self.level = level
        self.tag = tag
        self.value = value
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

    def find_sub_element(self, tag: str) -> list:
        """Find a sub element by tag.

        :param tag: The tag of the sub element to find.
        :type tag: str
        :return: The sub element found.
        :rtype: list
        """
        return [element for element in self.__sub_elements if element.tag == tag]

    def __str__(self) -> str:
        """Get the string representation of the Gedcom element.

        :return: The string representation of the Gedcom element.
        :rtype: str
        """
        return (
            "Level: "
            + str(self.level)
            + ", Tag: "
            + str(self.tag)
            + ", Value: "
            + str(self.value)
        )

    def __repr__(self) -> str:
        """Get the string representation of the Gedcom element.

        :return: The string representation of the Gedcom element.
        :rtype: str
        """
        return self.__str__()

    def export(self, empty_fields=True) -> dict:
        """Export the Gedcom element.

        :param empty_fields: Whether to export empty fields. Defaults to True.
        :type empty_fields: bool, optional
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
                    export_dict[export_key] = export_value.export(
                        empty_fields=empty_fields
                    )
                elif not export_value and not empty_fields:
                    pass
                else:
                    export_dict[export_key] = export_value if export_value else ""
        return export_dict
