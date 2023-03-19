class GedcomElement:
    def __init__(
        self,
        level: int,
        tag: str,
        sub_elements: list,
        value: str = None,
    ):
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
        chars = line.split(" ")
        level = int(chars.pop(0))
        xref = chars.pop(0) if chars[0].startswith("@") else None
        tag = chars.pop(0)
        value = " ".join(chars) if chars != [] else ""
        return {"level": level, "xref": xref, "tag": tag, "value": value}

    def get_sub_elements(self):
        return self.__sub_elements

    def find_sub_element(self, tag: str) -> list:
        return [element for element in self.__sub_elements if element.tag == tag]

    def __str__(self) -> str:
        return (
            "Level: "
            + str(self.level)
            + ", Tag: "
            + str(self.tag)
            + ", Value: "
            + str(self.value)
        )
