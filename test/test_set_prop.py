from ..src.pygedcom import gedcom_parser


def test_set_individual_name():
    parser = gedcom_parser.GedcomParser("test/samples/00_simple_individual_record.ged")
    parser.parse()
    assert parser.individuals[0].get_name() == "John /Doe/"
    assert parser.individuals[0].get_first_name() == "John"
    assert parser.individuals[0].get_last_name() == "Doe"
    parser.individuals[0].set_first_name("Jane")
    parser.individuals[0].set_last_name("Doe")
    assert parser.individuals[0].get_name() == "Jane /Doe/"
    assert parser.individuals[0].get_first_name() == "Jane"
    assert parser.individuals[0].get_last_name() == "Doe"


def test_set_individual_sex():
    parser = gedcom_parser.GedcomParser("test/samples/00_simple_individual_record.ged")
    parser.parse()
    assert parser.individuals[0].get_sex() == "M"
    parser.individuals[0].set_sex("F")
    assert parser.individuals[0].get_sex() == "F"
