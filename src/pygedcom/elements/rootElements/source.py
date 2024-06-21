from .rootElement import GedcomRootElement
import re


class GedcomSource(GedcomRootElement):
    """The Gedcom source element.

    :param level: The level of the Gedcom source.
    :type level: int
    :param xref: The xref of the Gedcom source.
    :type xref: str
    :param tag: The tag of the Gedcom source.
    :type tag: str
    :param sub_elements: The sub elements of the Gedcom source.
    :type sub_elements: list
    :return: The Gedcom source.
    :rtype: GedcomSource
    """

    def __init__(self, level: int, xref: str, tag: str, sub_elements: list):
        """Initialize the Gedcom source."""
        super().__init__(level, xref, tag, sub_elements)
        self.__export_quality = self.__find_quality()
        self.__export_title = self.__find_title()
        self.__export_type = self.__find_type()
        self.__export_repo = self.__find_repo()
        self.__export_object = self.__find_object()
        self.__export_media_type = self.__find_media_type()
        self.__export_note = self.__find_note()

    def __find_quality(self) -> str:
        """Find the quality of the Gedcom source.

        :return: The quality of the Gedcom source.
        :rtype: str
        """
        quality = self.find_sub_element("QUAY")
        if quality != []:
            return quality[0].get_value()
        return ""

    def __find_title(self):
        """Find the title of the Gedcom source.

        :return: The title of the Gedcom source.
        :rtype: str
        """
        title = self.find_sub_element("ABBR")
        if title != []:
            return title[0].get_value()
        return ""

    def __find_type(self):
        """Find the type of the Gedcom source.

        :return: The type of the Gedcom source.
        :rtype: str
        """
        type = self.find_sub_element("TYPE")
        if type != []:
            return type[0].get_value()
        return ""

    def __find_object(self):
        """Find the object of the Gedcom source.

        :return: The object of the Gedcom source.
        :rtype: str
        """
        object = self.find_sub_element("OBJE")
        if object != []:
            return object[0].get_value()
        return ""

    def __find_repo(self):
        """Find the repository of the Gedcom source.

        :return: The repository of the Gedcom source.
        :rtype: str
        """
        repo = self.find_sub_element("REPO")
        if repo != []:
            return repo[0].get_value()
        return ""

    def __find_media_type(self):
        """Find the media type of the Gedcom source.

        :return: The media type of the Gedcom source.
        :rtype: str
        """
        caln = self.find_sub_element("CALN")
        if caln != []:
            media_type = caln[0].find_sub_element("MEDI")
            if media_type != []:
                return media_type[0].get_value()
        return ""

    def __find_note(self):
        """Find the note of the Gedcom source.

        :return: The note of the Gedcom source.
        :rtype: str
        """
        rtf_pattern = re.compile(r"\\[a-z0-9]+")
        note = self.find_sub_element("NOTE")
        if note != []:
            content = note[0].find_sub_element("CONT")
            if content != []:
                # TODO: notes are still ugly.
                return re.sub(rtf_pattern, "", " ".join([cont.get_value() for cont in content]))
        return ""

    def get_quality(self) -> str:
        """Get the quality of the Gedcom source.

        :return: The quality of the Gedcom source.
        :rtype: str
        """
        return self.__export_quality

    def get_title(self) -> str:
        """Get the title of the Gedcom source.

        :return: The title of the Gedcom source.
        :rtype: str
        """
        return self.__export_title

    def get_type(self) -> str:
        """Get the type of the Gedcom source.

        :return: The type of the Gedcom source.
        :rtype: str
        """
        return self.__export_type

    def get_object(self) -> str:
        """Get the object of the Gedcom source.

        :return: The object of the Gedcom source.
        :rtype: str
        """
        return self.__export_object

    def get_repo(self) -> str:
        """Get the repository of the Gedcom source.

        :return: The repository of the Gedcom source.
        :rtype: str
        """
        return self.__export_repo

    def get_media_type(self) -> str:
        """Get the media type of the Gedcom source.

        :return: The media type of the Gedcom source.
        :rtype: str
        """
        return self.__export_media_type

    def get_note(self) -> str:
        """Get the note of the Gedcom source.

        :return: The note of the Gedcom source.
        :rtype: str
        """
        return self.__export_note
