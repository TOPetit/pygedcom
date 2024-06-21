import json

from .elements.rootElements.rootElement import GedcomRootElement
from .elements.rootElements.family import GedcomFamily
from .elements.rootElements.head import GedcomHead
from .elements.rootElements.individual import GedcomIndividual
from .elements.rootElements.object import GedcomObject
from .elements.rootElements.repository import GedcomRepository
from .elements.rootElements.source import GedcomSource
from .elements.rootElements.submitter import GedcomSubmitter
from .elements.rootElements.note import GedcomNote
from .elements.element import GedcomElement


class GedcomParser:
    """The GEDCOM parser main class.

    Use this class to initialize the parsing of a GEDCOM file.
    You can then verify, parse, access the elements and export the data.

    :param path: The path to the GEDCOM file.
    :type path: str
    :return: The GEDCOM parser.
    :rtype: GedcomParser
    """

    def __init__(self, path: str):
        self.path = path
        self.head = None
        self.individuals = []
        self.families = []
        self.sources = []
        self.objects = []
        self.repositories = []
        self.submitters = []
        self.notes = []
        self.isTRLR = False

    def __open(self) -> str:
        """Open the GEDCOM file and return the content.

        :return: The content of the GEDCOM file.
        :rtype: str
        """
        supported_encodings = ["utf-8", "utf-16", "latin1", "ansi"]
        for encoding in supported_encodings:
            try:
                with open(self.path, "r", encoding=encoding) as file:
                    return file.read()
            except UnicodeDecodeError:
                continue
        raise ValueError(
            f"Could not open file {self.path} with supported encodings ({', '.join(supported_encodings)})."
        )

    def __parse_line(self, line: str) -> dict:
        """Parse a line of a GEDCOM file.

        :param line: The line to parse.
        :type line: str
        :return: A dictionary with the level, the xref, the tag and the value.
        :rtype: dict
        """
        chars = line.split(" ")
        level = int(chars.pop(0))
        xref = chars.pop(0) if chars[0].startswith("@") else None
        tag = chars.pop(0)
        value = " ".join(chars) if chars != [] else ""
        return {"level": level, "xref": xref, "tag": tag, "value": value}

    def verify(self) -> dict:
        """Verify the file is a valid GEDCOM file. This only checks the level of each line, not the content.

        :return: A dictionary with the status and the message.
        :rtype: dict
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
                        "message": "Invalid level on line " + str(current_line) + ": " + line,
                    }
                current_level = parsed_line["level"]
        return {"status": "ok", "message": ""}

    def __create_element(self, parsed_line: dict, element_lines: list):
        """Create an element based on the parsed line and the element lines.

        :param parsed_line: The parsed line.
        :type parsed_line: dict
        :param element_lines: The lines of the element.
        :type element_lines: list
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
                "",  # No xref for HEAD
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
        elif parsed_line["tag"] == "TRLR":
            self.isTRLR = True
        elif parsed_line["tag"] == "SUBM":
            self.submitters.append(
                GedcomSubmitter(
                    parsed_line["level"],
                    parsed_line["xref"],
                    parsed_line["tag"],
                    element_lines,
                )
            )
        elif parsed_line["tag"] == "NOTE":
            self.notes.append(
                GedcomNote(
                    parsed_line["level"],
                    parsed_line["xref"],
                    parsed_line["tag"],
                    element_lines,
                )
            )

    def parse(self) -> dict:
        """Parse the GEDCOM file and return a dictionary with the parsed elements

        :return: A dictionary with the parsed elements.
        :rtype: dict
        """
        self.head = None
        self.submitters = []
        self.individuals = []
        self.families = []
        self.sources = []
        self.objects = []
        self.notes = []
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
            "head": self.head,
            "individuals": self.individuals,
            "submitters": self.submitters,
            "families": self.families,
            "sources": self.sources,
            "objects": self.objects,
            "notes": self.notes,
            "repositories": self.repositories,
        }

    def get_stats(self) -> dict:
        """Get statistics about the GEDCOM file.

        :return: A dictionary with the statistics.
        :rtype: dict
        """
        return {
            "head": "OK" if self.head is not None else "None",
            "submitters": len(self.submitters),
            "individuals": len(self.individuals),
            "families": len(self.families),
            "sources": len(self.sources),
            "objects": len(self.objects),
            "notes": len(self.notes),
            "repositories": len(self.repositories),
        }

    # define a helper function that recursively checks if a dictionary has only empty fields
    def __is_empty(self, d):
        """Check if a dictionary has only empty fields."""
        for v in d.values():
            if isinstance(v, dict):
                if not self.__is_empty(v):
                    return False
            elif v:
                return False
        return True

    # define a helper function that recursively removes empty fields
    def __remove_empty(self, d):
        """Remove empty fields from a dictionary."""
        for k in list(d.keys()):
            if isinstance(d[k], dict):
                self.__remove_empty(d[k])
                if self.__is_empty(d[k]):
                    del d[k]
            elif not d[k]:
                del d[k]

    def export(self, format: str = "json", empty_fields=True) -> str:
        """Export the GEDCOM file to another format.

        :param format: The format to export to. Default is "json".
        :type format: str
        :param empty_fields: If True, empty fields will be exported. Default is True.
        :type empty_fields: bool
        :return: The exported file's content.
        :rtype: str
        :raises ValueError: If the format is not supported.
        """
        if format not in ["json", "gedcom"]:
            raise ValueError("Format " + format + " is not supported.")
        if format == "json":
            export = {}
            if empty_fields or self.head:
                export["head"] = self.head.export() if self.head else ""
            if empty_fields or self.submitters:
                export["submitters"] = {}
                for submitter in self.submitters:
                    export["submitters"][submitter.get_xref()] = submitter.export()
            if empty_fields or self.individuals:
                export["individuals"] = {}
                for individual in self.individuals:
                    export["individuals"][individual.get_xref()] = individual.export()
            if empty_fields or self.families:
                export["families"] = {}
                for family in self.families:
                    export["families"][family.get_xref()] = family.export()
            if empty_fields or self.objects:
                export["objects"] = {}
                for object in self.objects:
                    export["objects"][object.get_xref()] = object.export()
            if empty_fields or self.notes:
                export["notes"] = {}
                for note in self.notes:
                    export["notes"][note.get_xref()] = note.export()
            if empty_fields or self.repositories:
                export["repositories"] = {}
                for repository in self.repositories:
                    export["repositories"][repository.get_xref()] = repository.export()
            if empty_fields or self.sources:
                export["sources"] = {}
                for source in self.sources:
                    export["sources"][source.get_xref()] = source.export()

            if not empty_fields:
                self.__remove_empty(export)
            return json.dumps(export, indent=4, ensure_ascii=False)
        if format == "gedcom":
            content = ""
            if self.head:
                content += self.head.extract_gedcom()
            for submitter in self.submitters:
                content += submitter.extract_gedcom()
            for individual in self.individuals:
                content += individual.extract_gedcom()
            for family in self.families:
                content += family.extract_gedcom()
            for object in self.objects:
                content += object.extract_gedcom()
            for note in self.notes:
                content += note.extract_gedcom()
            for repository in self.repositories:
                content += repository.extract_gedcom()
            for source in self.sources:
                content += source.extract_gedcom()
            content += "0 TRLR\n" if self.isTRLR else ""
            return content

    def get_parents(self, individual: GedcomIndividual) -> list:
        """Get the parents of an individual.

        :param individual: The individual to get the parents of.
        :type individual: GedcomIndividual
        :return: A list of GedcomIndividual objects.
        :rtype: list
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

        :param individual: The individual to get the children of.
        :type individual: GedcomIndividual
        :return: A list of GedcomIndividual objects.
        :rtype: list
        """
        children = []
        for family in self.families:
            if individual.get_xref() in family.get_parents():
                for child in family.get_children():
                    children.append(self.find_individual(child))
        return children

    def __find_root_element(self, collection: list, xref: str) -> GedcomElement:
        """Find an element in a collection by its xref.

        :param collection: The collection to search in.
        :type collection: list
        :param xref: The xref to search for.
        :type xref: str
        :return: The element if found, None otherwise.
        :rtype: GedcomElement
        """
        for element in collection:
            if element.get_xref() == xref:
                return element
        raise KeyError("Element with xref " + xref + " not found.")

    def find_individual(self, xref: str) -> GedcomIndividual:
        """Find an individual by its xref.

        :param xref: The xref to search for.
        :type xref: str
        :return: The individual if found, None otherwise.
        :rtype: GedcomIndividual
        """
        return self.__find_root_element(self.individuals, xref)

    def find_family(self, xref: str) -> GedcomFamily:
        """Find a family by its xref.

        :param xref: The xref to search for.
        :type xref: str
        :return: The family if found, None otherwise.
        :rtype: GedcomFamily
        """
        return self.__find_root_element(self.families, xref)

    def find_source(self, xref: str) -> GedcomSource:
        """Find a source by its xref.

        :param xref: The xref to search for.
        :type xref: str
        :return: The source if found, None otherwise.
        :rtype: GedcomSource
        """
        return self.__find_root_element(self.sources, xref)

    def find_object(self, xref: str) -> GedcomObject:
        """Find an object by its xref.

        :param xref: The xref to search for.
        :type xref: str
        :return: The object if found, None otherwise.
        :rtype: GedcomObject
        """
        return self.__find_root_element(self.objects, xref)

    def find_repository(self, xref: str) -> GedcomRepository:
        """Find a repository by its xref.

        :param xref: The xref to search for.
        :type xref: str
        :return: The repository if found, None otherwise.
        :rtype: GedcomRepository
        """
        return self.__find_root_element(self.repositories, xref)

    def __add_root_element(self, collection: list, element: GedcomRootElement):
        """Add an element to a collection.

        :param collection: The collection to add the element to.
        :type collection: list
        :param element: The element to add.
        :type element: GedcomRootElement
        :raises KeyError: If the element already exists.
        """
        try:
            self.__find_root_element(collection, element.get_xref())
        except KeyError:
            collection.append(element)
        else:
            raise KeyError("Element with xref " + element.get_xref() + " already exists.")

    def add_individual(self, individual: GedcomIndividual):
        """Add an individual to the collection.

        :param individual: The individual to add.
        :type individual: GedcomIndividual
        :raises KeyError: If the individual already exists.
        :raises TypeError: If the individual is not of type GedcomIndividual.
        """
        if not isinstance(individual, GedcomIndividual):
            raise TypeError("Individual must be of type GedcomIndividual.")
        try:
            self.__add_root_element(self.individuals, individual)
        except KeyError:
            raise KeyError("Individual with xref " + individual.get_xref() + " already exists.")

    def add_family(self, family: GedcomFamily):
        """Add a family to the collection.

        This checks :
            - if the family passed is of type GedcomFamily.
            - if the family passed does not already exist (by xref).
            - if every parent and child exists (their xref are in the individual collection).


        :param family: The family to add.
        :type family: GedcomFamily
        :raises KeyError: If the family already exists.
        :raises TypeError: If the family is not of type GedcomFamily.
        """
        if self.find_individual(family.get_husband()) is None:
            raise KeyError("Husband with xref " + family.get_husband() + " not found.")
        if self.find_individual(family.get_wife()) is None:
            raise KeyError("Wife with xref " + family.get_wife() + " not found.")
        for child in family.get_children():
            if self.find_individual(child) is None:
                raise KeyError("Child with xref " + child + " not found.")
        if not isinstance(family, GedcomFamily):
            raise TypeError("Family must be of type GedcomFamily.")
        try:
            self.__add_root_element(self.families, family)
        except KeyError:
            raise KeyError("Family with xref " + family.get_xref() + " already exists.")

    def add_source(self, source: GedcomSource):
        """Add a source to the collection.

        :param source: The source to add.
        :type source: GedcomSource
        :raises KeyError: If the source already exists.
        :raises TypeError: If the source is not of type GedcomSource.
        """
        if not isinstance(source, GedcomSource):
            raise TypeError("Source must be of type GedcomSource.")
        try:
            self.__add_root_element(self.sources, source)
        except KeyError:
            raise KeyError("Source with xref " + source.get_xref() + " already exists.")
        self.sources.append(source)

    def add_object(self, object: GedcomObject):
        """Add an object to the collection.

        :param object: The object to add.
        :type object: GedcomObject
        :raises KeyError: If the object already exists.
        :raises TypeError: If the object is not of type GedcomObject.
        """
        if not isinstance(object, GedcomObject):
            raise TypeError("Object must be of type GedcomObject.")
        try:
            self.__add_root_element(self.objects, object)
        except KeyError:
            raise KeyError("Object with xref " + object.get_xref() + " already exists.")
        self.objects.append(object)

    def add_repository(self, repository: GedcomRepository):
        """Add a repository to the collection.

        :param repository: The repository to add.
        :type repository: GedcomRepository
        :raises KeyError: If the repository already exists.
        :raises TypeError: If the repository is not of type GedcomRepository.
        """
        if not isinstance(repository, GedcomRepository):
            raise TypeError("Repository must be of type GedcomRepository.")
        try:
            self.__add_root_element(self.repositories, repository)
        except KeyError:
            raise KeyError("Repository with xref " + repository.get_xref() + " already exists.")
        self.repositories.append(repository)

    def __remove_root_element(self, collection: list, xref: str):
        """Remove an element from a collection.

        :param collection: The collection to remove the element from.
        :type collection: list
        :param xref: The xref of the element to remove.
        :type xref: str
        :raises KeyError: If the element does not exist.
        """
        element = self.__find_root_element(collection, xref)
        if not element:
            raise KeyError()
        collection.remove(element)

    def remove_individual(self, xref: str):
        """Remove an individual from the collection and all mentions of it in families.

        :param xref: The xref of the individual to remove.
        :type xref: str
        :raises KeyError: If the individual does not exist.
        """
        try:
            individual = self.find_individual(xref)
        except KeyError:
            raise KeyError("Individual with xref " + xref + " does not exist.")

        xref = individual.get_xref()

        for family in self.families:
            family.remove_parent(xref)
            family.remove_child(xref)

        self.__remove_root_element(self.individuals, xref)

    def remove_family(self, xref: str):
        """Remove a family from the collection.

        :param xref: The xref of the family to remove.
        :type xref: str
        :raises KeyError: If the family does not exist.
        """
        try:
            family = self.find_family(xref)
        except KeyError:
            raise KeyError("Family with xref " + xref + " does not exist.")

        xref = family.get_xref()

        for individual in self.individuals:
            individual.remove_family(xref)

        self.__remove_root_element(self.families, xref)
