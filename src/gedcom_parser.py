import json
from .elements.family import GedcomFamily
from .elements.head import GedcomHead
from .elements.individual import GedcomIndividual
from .elements.object import GedcomObject
from .elements.repository import GedcomRepository
from .elements.source import GedcomSource
from .elements.element import GedcomElement


class GedcomParser:
    """The GEDCOM parser."""

    def __init__(self, path: str):
        """Initialize the GEDCOM parser.

        Args:
            path (str): The path to the GEDCOM file.
        """
        self.path = path
        self.head = None
        self.individuals = []
        self.families = []
        self.sources = []
        self.objects = []
        self.repositories = []

    def __open(self) -> str:
        """Open the GEDCOM file and return the content.

        Returns:
            str: The content of the GEDCOM file.
        """
        with open(self.path, "r") as file:
            data = file.read()
        return data

    def __parse_line(self, line: str) -> dict:
        """Parse a line of a GEDCOM file.

        Args:
            line (str): The line to parse.

        Returns:
            dict: A dictionary with the level, xref, tag and value.
        """
        chars = line.split(" ")
        level = int(chars.pop(0))
        xref = chars.pop(0) if chars[0].startswith("@") else None
        tag = chars.pop(0)
        value = " ".join(chars) if chars != [] else ""
        return {"level": level, "xref": xref, "tag": tag, "value": value}

    def verify(self) -> dict:
        """Verify the file is a valid GEDCOM file. This only checks the level of each line, not the content.

        Returns:
            dict: A dictionary with the status and a message. Status can be "ok" or "error".
        """
        file = self.__open()
        lines = file.split("\n")
        current_level = 0
        current_line = 0
        for line in lines:
            current_line += 1
            if line != "":
                # Check if the level is valid
                parsed_line = self.__parse_line(line)
                if parsed_line["level"] > current_level + 1:
                    return {
                        "status": "error",
                        "message": "Invalid level on line "
                        + str(current_line)
                        + ": "
                        + line,
                    }
                current_level = parsed_line["level"]
        return {"status": "ok", "message": ""}

    def __create_element(self, parsed_line: dict, element_lines: list):
        """Create an element based on the parsed line and the element lines.

        Args:
            parsed_line (dict): The parsed line.
            element_lines (list): The lines of the element.
        """
        if parsed_line["tag"] == "INDI":
            self.individuals.append(
                GedcomIndividual(
                    parsed_line["level"],
                    parsed_line["xref"],
                    parsed_line["tag"],
                    element_lines,
                )
            )
        elif parsed_line["tag"] == "FAM":
            self.families.append(
                GedcomFamily(
                    parsed_line["level"],
                    parsed_line["xref"],
                    parsed_line["tag"],
                    element_lines,
                )
            )
        elif parsed_line["tag"] == "HEAD":
            self.head = GedcomHead(
                parsed_line["level"],
                parsed_line["tag"],
                element_lines,
            )
        elif parsed_line["tag"] == "SOUR":
            self.sources.append(
                GedcomSource(
                    parsed_line["level"],
                    parsed_line["xref"],
                    parsed_line["tag"],
                    element_lines,
                )
            )
        elif parsed_line["tag"] == "REPO":
            self.repositories.append(
                GedcomRepository(
                    parsed_line["level"],
                    parsed_line["xref"],
                    parsed_line["tag"],
                    element_lines,
                )
            )
        elif parsed_line["tag"] == "OBJE":
            self.objects.append(
                GedcomObject(
                    parsed_line["level"],
                    parsed_line["xref"],
                    parsed_line["tag"],
                    element_lines,
                )
            )

    def parse(self) -> dict:
        """Parse the GEDCOM file and return a dictionary with the parsed elements

        Returns:
            dict -- Dictionary with the parsed elements
        """
        self.head = None
        self.individuals = []
        self.families = []
        self.sources = []
        self.objects = []
        self.repositories = []
        file = self.__open()
        lines = file.split("\n")
        current_parsed_line = self.__parse_line(lines[0])
        element_lines = []
        if lines != []:
            for line in lines[1:]:
                if line != "":
                    tmp_parsed_line = self.__parse_line(line)
                    if tmp_parsed_line["level"] > 0:
                        element_lines.append(line)
                    else:
                        self.__create_element(current_parsed_line, element_lines)
                        current_parsed_line = tmp_parsed_line
                        element_lines = []
            self.__create_element(current_parsed_line, element_lines)
        return {
            "individuals": self.individuals,
            "families": self.families,
            "sources": self.sources,
            "objects": self.objects,
            "repositories": self.repositories,
        }

    def get_stats(self) -> dict:
        """Get statistics about the GEDCOM file.

        Returns:
            dict -- Dictionary with the statistics.
        """
        return {
            "head": "OK" if self.head is not None else "None",
            "individuals": len(self.individuals),
            "families": len(self.families),
            "sources": len(self.sources),
            "objects": len(self.objects),
            "repositories": len(self.repositories),
        }

    def export(self, format: str = "json") -> str:
        """Export the GEDCOM file to another format.

        Args:
            format (str, optional): The format to export to. Defaults to "json".

        Returns:
            str -- The exported json string.
        """
        if format == "json":
            data = {
                "individuals": {},
                "families": {},
                "sources": {},
                "objects": {},
                "repositories": {},
            }
            for individual in self.individuals:
                data["individuals"][individual.get_xref()] = individual.get_data()

            for family in self.families:
                data["families"][family.get_xref()] = family.get_data()

            for source in self.sources:
                data["sources"][source.get_xref()] = source.get_data()

            for object in self.objects:
                data["objects"][object.get_xref()] = object.get_data()

            for repository in self.repositories:
                data["repositories"][repository.get_xref()] = repository.get_data()

            return json.dumps(data, indent=4, ensure_ascii=False)

    def get_parents(self, individual: GedcomIndividual) -> list:
        """Get the parents of an individual.

        Args:
            individual (GedcomIndividual): The individual to get the parents of.

        Returns:
            list: A list of GedcomIndividual objects.
        """
        parents = []
        for family in self.families:
            if individual.get_xref() in family.get_children():
                if family.get_husband() != "":
                    parents.append(self.find_individual(family.get_husband()))
                if family.get_wife() != "":
                    parents.append(self.find_individual(family.get_wife()))
        return parents

    def get_children(self, individual: GedcomIndividual) -> list:
        """Get the children of an individual.

        Args:
            individual (GedcomIndividual): The individual to get the children of.

        Returns:
            list: A list of GedcomIndividual objects.
        """
        children = []
        for family in self.families:
            if individual.get_xref() in family.get_parents():
                for child in family.get_children():
                    children.append(self.find_individual(child))
        return children

    def __find_root_element(self, collection: list, xref: str) -> GedcomElement:
        """Find an element in a collection by its xref.

        Args:
            collection (list): The collection to search in.
            xref (str): The xref to search for.

        Returns:
            GedcomElement: The element if found, None otherwise.
        """
        for element in collection:
            if element.get_xref() == xref:
                return element
        return None

    def find_individual(self, xref: str) -> GedcomIndividual:
        """Find an individual by its xref.

        Args:
            xref (str): The xref to search for.

        Returns:
            GedcomIndividual: The individual if found, None otherwise.
        """
        return self.__find_root_element(self.individuals, xref)

    def find_family(self, xref: str) -> GedcomFamily:
        """Find a family by its xref.

        Args:
            xref (str): The xref to search for.

        Returns:
            GedcomFamily: The family if found, None otherwise.
        """
        return self.__find_root_element(self.families, xref)

    def find_source(self, xref: str) -> GedcomSource:
        """Find a source by its xref.

        Args:
            xref (str): The xref to search for.

        Returns:
            GedcomSource: The source if found, None otherwise.
        """
        return self.__find_root_element(self.sources, xref)

    def find_object(self, xref: str) -> GedcomObject:
        """Find an object by its xref.

        Args:
            xref (str): The xref to search for.

        Returns:
            GedcomObject: The object if found, None otherwise.
        """
        return self.__find_root_element(self.objects, xref)

    def find_repository(self, xref: str) -> GedcomRepository:
        """Find a repository by its xref.

        Args:
            xref (str): The xref to search for.

        Returns:
            GedcomRepository: The repository if found, None otherwise.
        """
        return self.__find_root_element(self.repositories, xref)
