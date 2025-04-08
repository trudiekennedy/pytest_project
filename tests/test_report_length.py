from lib.report_length import *

def test_report_length_bananas():
    result = report_length("bananas!")
    assert result == "This string was 8 characters long."

def test_report_length_discombulated():
    result = report_length("discombulated")
    assert result == "This string was 13 characters long."

def test_report_length_you():
    result = report_length("you")
    assert result == "This string was 3 characters long."