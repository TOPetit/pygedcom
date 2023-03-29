import json
from src import gedcom_parser


def test_export_00():
    parser = gedcom_parser.GedcomParser("test/samples/00_simple_individual_record.ged")
    parser.parse()
    result = json.loads(parser.export())
    assert result["individuals"]["@I1@"]["name"] == "John /Doe/"
    assert result["individuals"]["@I1@"]["first_name"] == "John"
    assert result["individuals"]["@I1@"]["last_name"] == "Doe"
    assert result["individuals"]["@I1@"]["date_of_birth"]["day"] == "01"
    assert result["individuals"]["@I1@"]["date_of_birth"]["month"] == "JAN"
    assert result["individuals"]["@I1@"]["date_of_birth"]["year"] == "1900"
    assert result["individuals"]["@I1@"]["date_of_death"]["day"] == "01"
    assert result["individuals"]["@I1@"]["date_of_death"]["month"] == "JAN"
    assert result["individuals"]["@I1@"]["date_of_death"]["year"] == "1970"


def test_export_01():
    parser = gedcom_parser.GedcomParser("test/samples/01_simple_family_record.ged")
    parser.parse()
    result = json.loads(parser.export())
    assert result["families"]["@F1@"]["husband"] == "@I1@"
    assert result["families"]["@F1@"]["wife"] == "@I2@"
    assert result["families"]["@F1@"]["children"] == ["@I3@"]
    assert result["families"]["@F1@"]["marriage_date"]["day"] == "01"
    assert result["families"]["@F1@"]["marriage_date"]["month"] == "JAN"
    assert result["families"]["@F1@"]["marriage_date"]["year"] == "1925"
