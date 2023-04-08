from ..src.pygedcom import gedcom_parser


def test_verify_00():
    parser = gedcom_parser.GedcomParser("test/samples/00_simple_individual_record.ged")
    result = parser.verify()
    assert result["status"] == "ok"
    assert result["message"] == ""


def test_verify_01():
    parser = gedcom_parser.GedcomParser("test/samples/01_simple_family_record.ged")
    result = parser.verify()
    assert result["status"] == "ok"
    assert result["message"] == ""


def test_verify_02():
    parser = gedcom_parser.GedcomParser("test/samples/02_simple_source_record.ged")
    result = parser.verify()
    assert result["status"] == "ok"
    assert result["message"] == ""


def test_verify_03():
    parser = gedcom_parser.GedcomParser("test/samples/03_simple_repository_record.ged")
    result = parser.verify()
    assert result["status"] == "ok"
    assert result["message"] == ""


def test_verify_04():
    parser = gedcom_parser.GedcomParser("test/samples/04_simple_date_formats.ged")
    result = parser.verify()
    assert result["status"] == "ok"
    assert result["message"] == ""


def test_verify_10():
    parser = gedcom_parser.GedcomParser("test/samples/10_invalid_level.ged")
    result = parser.verify()
    assert result["status"] == "error"
    assert result["message"] == "Invalid level on line 4: 3 DATE 01 JAN 1900"


def test_verify_20():
    parser = gedcom_parser.GedcomParser("test/samples/20_complex_sample.ged")
    result = parser.verify()
    assert result["status"] == "ok"
