class GedcomElement():
    def __init__(self, level: int, tag: str, value: str, sub_elements: list):
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
                    self.__sub_elements.append(GedcomElement(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
                    current_parsed_line = tmp_parsed_line
                    element_lines = []
            self.__sub_elements.append(GedcomElement(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))

    def __parse_line(self, line: str) -> dict:
        chars = line.split(' ')
        level = int(chars[0])
        tag = chars[1]
        value = ' '.join(chars[2:]) if len(chars) > 2 else ""
        return {"level": level, "tag": tag, "value": value}

    def get_sub_elements(self):
        return self.__sub_elements
    
    def __str__(self) -> str:
        return "Level: " + str(self.level) + ", Tag: " + str(self.tag) + ", Value: " + str(self.value)