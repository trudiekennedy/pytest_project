import pytest
from lib.present import *

def test_present_not_none_updates_contents():
    present = Present()
    present.wrap("hello")
    assert present.contents == "hello"


def test_contents_is_none_as_default():
    present = Present()
    assert present.contents == None


def test_wrap_exception_where_contents_not_none():
    present = Present()
    present.wrap("goodbye")
    with pytest.raises(Exception) as e:
        present.wrap("hello")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


def test_unwrap_where_contents_none():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

