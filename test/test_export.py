import json
from ..src.pygedcom import gedcom_parser


def test_export_00():
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


def test_export_01():
    parser = gedcom_parser.GedcomParser("test/samples/01_simple_family_record.ged")
    parser.parse()
    result = json.loads(parser.export())
    assert result["families"]["@F1@"]["husband"] == "@I1@"
    assert result["families"]["@F1@"]["wife"] == "@I2@"
    assert result["families"]["@F1@"]["children"] == ["@I3@"]
    assert result["families"]["@F1@"]["marriage"]["date"]["day"] == "01"
    assert result["families"]["@F1@"]["marriage"]["date"]["month"] == "JAN"
    assert result["families"]["@F1@"]["marriage"]["date"]["year"] == "1925"


def test_export_20():
    parser = gedcom_parser.GedcomParser("test/samples/20_complex_sample.ged")
    parser.parse()
    result = json.loads(parser.export())
    assert result["individuals"]["@1@"]["name"] == "Robert Eugene/Williams/"
    assert result["individuals"]["@1@"]["birth"]["date"]["day"] == "02"
    assert result["individuals"]["@1@"]["birth"]["date"]["month"] == "OCT"
    assert result["individuals"]["@1@"]["birth"]["date"]["year"] == "1822"
    assert result["individuals"]["@1@"]["sex"] == "M"
    assert result["individuals"]["@1@"]["death"]["date"]["day"] == "14"
    assert result["individuals"]["@1@"]["death"]["date"]["month"] == "APR"
    assert result["individuals"]["@1@"]["death"]["date"]["year"] == "1905"
