import json
from ..src.pygedcom import gedcom_parser
from ..src.pygedcom.elements.rootElements.individual import GedcomIndividual


def test_add_individual():
    parser = gedcom_parser.GedcomParser("test/samples/00_simple_individual_record.ged")
    parser.parse()
    newIndividual = GedcomIndividual(0, "@I2@", "INDI", [])
    newIndividual.set_first_name("John")
    newIndividual.set_last_name("Wick")
    parser.add_individual(newIndividual)
    assert len(parser.individuals) == 2
    assert parser.individuals[1].get_xref() == "@I2@"
    assert parser.individuals[1].get_first_name() == "John"
    assert parser.individuals[1].get_last_name() == "Wick"
    result = json.loads(parser.export())
    assert result["individuals"]["@I1@"]["name"] == "John /Doe/"
    assert result["individuals"]["@I1@"]["first_name"] == "John"
    assert result["individuals"]["@I1@"]["last_name"] == "Doe"
    assert result["individuals"]["@I1@"]["birth"]["date"]["day"] == "01"
    assert result["individuals"]["@I1@"]["birth"]["date"]["month"] == "JAN"
    assert result["individuals"]["@I1@"]["birth"]["date"]["year"] == "1900"
    assert result["individuals"]["@I1@"]["death"]["date"]["day"] == "01"
    assert result["individuals"]["@I1@"]["death"]["date"]["month"] == "JAN"
    assert result["individuals"]["@I1@"]["death"]["date"]["year"] == "1970"
    assert result["individuals"]["@I2@"]["name"] == "John /Wick/"
    assert result["individuals"]["@I2@"]["first_name"] == "John"
    assert result["individuals"]["@I2@"]["last_name"] == "Wick"
