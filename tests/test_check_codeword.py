from lib.check_codeword import *

# Tests the correct word

def test_check_codeword_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# Tests a word that begins with h and ends with e

def test_check_codeword_hose():
    result = check_codeword("hose")
    assert result == "Close, but nope."

# Tests a completely wrong code word

def test_check_codeword_bananas():
    result = check_codeword("bananas!")
    assert result == "WRONG!"

# Tests a word that begins with h but doesn't end in e (so should be wrong)    

def test_check_codeword_helmet():
    result = check_codeword("helmet")
    assert result == "WRONG!"

# Tests a word that doesn't begin with h but ends in e (so should be wrong)    

def test_check_codeword_shame():
    result = check_codeword('shame')
    assert result == "WRONG!"