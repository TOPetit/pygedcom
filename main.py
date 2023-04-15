import json
from src.pygedcom import gedcom_parser

parser = gedcom_parser.GedcomParser(path="private/Theo-Export.ged")
print(parser.verify())

data = parser.parse()

print(parser.get_stats())

json_string = parser.export(format="json", empty_fields=True)
with open("private/test.json", "w") as file:
    file.write(json_string)


gedcom_string = parser.export(format="gedcom", empty_fields=False)
with open("private/test.ged", "w") as file:
    file.write(gedcom_string)
