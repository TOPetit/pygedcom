from src import gedcom_parser

parser = gedcom_parser.GedcomParser(path="private/Theo-Export.ged")
print(parser.verify())

data = parser.parse()

print(parser.get_stats())
