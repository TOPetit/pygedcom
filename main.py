from src import gedcom_parser

parser = gedcom_parser.GedcomParser(path="private/Theo-Export.ged")
print(parser.verify())
parser.parse()

for individual in parser.individuals:
    print(individual)
