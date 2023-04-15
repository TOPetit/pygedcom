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


def test_export_json_empty_fields_20():
    parser = gedcom_parser.GedcomParser("test/samples/20_complex_sample.ged")
    parser.parse()
    result = json.loads(parser.export())
    john = result["individuals"]["@I0001@"]
    assert "birth" in john
    assert "death" in john
    assert "name" in john
    assert "first_name" in john
    assert "last_name" in john
    assert "sex" in john
    assert "media" in john
    assert "date" in john["birth"]
    assert "day" in john["birth"]["date"]
    assert "month" in john["birth"]["date"]
    assert "year" in john["birth"]["date"]
    assert "place" in john["birth"]
    assert "map" in john["birth"]["place"]
    assert "latitude" in john["birth"]["place"]["map"]
    assert "longitude" in john["birth"]["place"]["map"]
    assert "place_infos" in john["birth"]["place"]
    assert "date" in john["death"]
    assert "day" in john["death"]["date"]
    assert "month" in john["death"]["date"]
    assert "year" in john["death"]["date"]
    assert "place" in john["death"]
    assert "map" in john["death"]["place"]
    assert "latitude" in john["death"]["place"]["map"]
    assert "longitude" in john["death"]["place"]["map"]
    assert "place_infos" in john["death"]["place"]


def test_export_json_no_empty_fields_20():
    parser = gedcom_parser.GedcomParser("test/samples/20_complex_sample.ged")
    parser.parse()
    result = json.loads(parser.export(empty_fields=False))
    john = result["individuals"]["@I0001@"]
    assert "birth" in john
    assert "death" not in john
    assert "name" in john
    assert "first_name" in john
    assert "last_name" in john
    assert "date" in john["birth"]
    assert "day" in john["birth"]["date"]
    assert "month" in john["birth"]["date"]
    assert "year" in john["birth"]["date"]
    assert "place" in john["birth"]
    assert "map" not in john["birth"]["place"]
    assert "place_infos" in john["birth"]["place"]


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
