from .elements.family import GedcomFamily
from .elements.head import GedcomHead
from .elements.individual import GedcomIndividual
from .elements.object import GedcomObject
from .elements.repository import GedcomRepository
from .elements.source import GedcomSource


class GedcomParser():

    def __init__(self, path: str):
        self.path = path

    def __open(self) -> str:
        with open(self.path, "r") as file:
            data = file.read()
        return data
    
    def __parse_line(self, line: str) -> dict:
        chars = line.split(' ')
        level = int(chars[0])
        tag = chars[1]
        value = ' '.join(chars[2:]) if len(chars) > 2 else ""
        return {"level": level, "tag": tag, "value": value}
    
    def __parse_lowlevel_line(self, line: str) -> dict:
        chars = line.split(' ')
        level = int(chars[0])
        value = chars[1]
        tag = chars[2] if len(chars) > 2 else ""
        return {"level": level, "tag": tag, "value": value}

    def verify(self) -> dict:
        file = self.__open()
        lines = file.split('\n')
        current_level = 0
        current_line = 0
        for line in lines:
            current_line += 1
            if line != "":
                # Check if the level is valid
                parsed_line = self.__parse_line(line)
                if parsed_line["level"] > current_level + 1:
                    return {"status": "error", "message": "Invalid level on line " + str(current_line) + ": " + line}
                current_level = parsed_line["level"]
        return {"status": "ok", "message": ""}
    
    def parse(self) -> None:
        self.head = None
        self.individuals = []
        self.families = []
        self.sources = []
        self.objects = []
        self.repositories = []
        file = self.__open()
        lines = file.split('\n')
        current_parsed_line = self.__parse_lowlevel_line(lines[0])
        element_lines = []
        if lines != []:
            for line in lines[1:]:
                if line != "":
                    tmp_parsed_line = self.__parse_lowlevel_line(line)
                    if tmp_parsed_line["level"] > 0:
                        element_lines.append(line)
                    else:
                        if current_parsed_line["tag"] == "INDI":
                            self.individuals.append(GedcomIndividual(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
                        elif current_parsed_line["tag"] == "FAM":
                            self.families.append(GedcomFamily(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
                        elif current_parsed_line["tag"] == "HEAD":
                            self.head = GedcomHead(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines)
                        elif current_parsed_line["tag"] == "SOUR":
                            self.sources.append(GedcomSource(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
                        elif current_parsed_line["tag"] == "REPO":
                            self.repositories.append(GedcomRepository(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
                        elif current_parsed_line["tag"] == "OBJE":
                            self.objects.append(GedcomObject(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
                        current_parsed_line = tmp_parsed_line
                        element_lines = []
            if current_parsed_line["tag"] == "INDI":
                self.individuals.append(GedcomIndividual(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
            elif current_parsed_line["tag"] == "FAM":
                self.families.append(GedcomFamily(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
            elif current_parsed_line["tag"] == "HEAD":
                self.head = GedcomHead(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines)
            elif current_parsed_line["tag"] == "SOUR":
                self.sources.append(GedcomSource(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
            elif current_parsed_line["tag"] == "REPO":
                self.repositories.append(GedcomRepository(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
            elif current_parsed_line["tag"] == "OBJE":
                self.objects.append(GedcomObject(current_parsed_line["level"], current_parsed_line["tag"], current_parsed_line["value"], element_lines))
