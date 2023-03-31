class GedcomElement:
    """Class for representing a Gedcom element."""

    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
        """Initialize the Gedcom element.

        Args:
            level (int): The level of the Gedcom element.
            tag (str): The tag of the Gedcom element.
            sub_elements (list): The sub elements of the Gedcom element.
            value (str, optional): The value of the Gedcom element. Defaults to None.

        Returns:
            GedcomElement: The Gedcom element.
        """
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

        Args:
            line (str): The line to parse. Result contains the level, xref, tag and value.

        Returns:
            dict: The parsed line.
        """
        chars = line.split(" ")
        level = int(chars.pop(0))
        xref = chars.pop(0) if chars[0].startswith("@") else None
        tag = chars.pop(0)
        value = " ".join(chars) if chars != [] else ""
        return {"level": level, "xref": xref, "tag": tag, "value": value}

    def get_sub_elements(self):
        """Get the sub elements of the Gedcom element.

        Returns:
            list: The sub elements of the Gedcom element as GedcomElements.
        """
        return self.__sub_elements

    def find_sub_element(self, tag: str) -> list:
        """Find a sub element by tag.

        Args:
            tag (str): The tag of the sub element.

        Returns:
            list: The sub elements of the Gedcom element as GedcomElements with the given tag.
        """
        return [element for element in self.__sub_elements if element.tag == tag]

    def __str__(self) -> str:
        """Get the string representation of the Gedcom element.

        Returns:
            str: The string representation of the Gedcom element.
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

        Returns:
            str: The string representation of the Gedcom element.
        """
        return self.__str__()
