from src import gedcom_parser

parser = gedcom_parser.GedcomParser(path="private/Theo-Export.ged")
print(parser.verify())

print(parser.get_stats())

parser.parse()

print(parser.get_stats())
