from lib.string_builder import *

# Tests that when nothing passed, an empty string is returned

def test_string_builder_nothing():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ''

# Tests that when nothing passed, an length is zero

def test_string_builder_nothing2():
    string_builder = StringBuilder()
    result = string_builder.size()
    assert result == 0

# Tests what happens when one string is added

def test_string_builder_one_word():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.output()
    assert result == "Hello"

# Checks the length of one word

def test_string_builder_one_word_len():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.size()
    assert result == 5

# Tests two words being added
def test_string_builder_two_words():
    string_builder = StringBuilder()
    string_builder.add("Bonjour")
    string_builder.add(" le monde!")
    result = string_builder.output()
    assert result == "Bonjour le monde!"

# Tests two words length
def test_string_builder_two_words_len():
    string_builder = StringBuilder()
    string_builder.add("Bonjour")
    string_builder.add(" le monde!")
    result = string_builder.size()
    assert result == 17