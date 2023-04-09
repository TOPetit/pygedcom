import json
from ..src.pygedcom import gedcom_parser


def test_export_json_00():
    parser = gedcom_parser.GedcomParser("test/samples/00_simple_individual_record.ged")
    parser.parse()
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


def test_export_json_01():
    parser = gedcom_parser.GedcomParser("test/samples/01_simple_family_record.ged")
    parser.parse()
    result = json.loads(parser.export())
    assert result["families"]["@F1@"]["husband"] == "@I1@"
    assert result["families"]["@F1@"]["wife"] == "@I2@"
    assert result["families"]["@F1@"]["children"] == ["@I3@"]
    assert result["families"]["@F1@"]["marriage"]["date"]["day"] == "01"
    assert result["families"]["@F1@"]["marriage"]["date"]["month"] == "JAN"
    assert result["families"]["@F1@"]["marriage"]["date"]["year"] == "1925"


def test_export_json_20():
    parser = gedcom_parser.GedcomParser("test/samples/20_complex_sample.ged")
    parser.parse()
    result = json.loads(parser.export())
    assert result["individuals"]["@I0001@"]["name"] == "John /Smith/"
    assert result["individuals"]["@I0001@"]["first_name"] == "John"
    assert result["individuals"]["@I0001@"]["last_name"] == "Smith"
    assert result["individuals"]["@I0001@"]["birth"]["date"]["day"] == "1"
    assert result["individuals"]["@I0001@"]["birth"]["date"]["month"] == "JAN"
    assert result["individuals"]["@I0001@"]["birth"]["date"]["year"] == "1900"
    assert result["individuals"]["@I0002@"]["name"] == "Jane /Doe/"
    assert result["individuals"]["@I0002@"]["first_name"] == "Jane"
    assert result["individuals"]["@I0002@"]["last_name"] == "Doe"
    assert result["individuals"]["@I0002@"]["birth"]["date"]["day"] == "05"
    assert result["individuals"]["@I0002@"]["birth"]["date"]["month"] == "FEB"
    assert result["individuals"]["@I0002@"]["birth"]["date"]["year"] == "1901"

    assert result["families"]["@F0001@"]["husband"] == "@I0001@"
    assert result["families"]["@F0001@"]["wife"] == "@I0002@"
    assert result["families"]["@F0001@"]["children"] == ["@I0003@"]


def test_export_gedcom_00():
    parser = gedcom_parser.GedcomParser("test/samples/00_simple_individual_record.ged")
    parser.parse()
    result = parser.export(format="gedcom")
    with open("test/samples/00_simple_individual_record.ged") as f:
        assert result == f.read()


def test_export_gedcom_01():
    parser = gedcom_parser.GedcomParser("test/samples/01_simple_family_record.ged")
    parser.parse()
    result = parser.export(format="gedcom")
    with open("test/samples/01_simple_family_record.ged") as f:
        assert result == f.read()


def test_export_gedcom_20():
    parser = gedcom_parser.GedcomParser("test/samples/20_complex_sample.ged")
    parser.parse()
    result = parser.export(format="gedcom")
    with open("test/samples/20_complex_sample.ged") as f:
        assert result == f.read()
