from lib.greet import *

def test_greeting_for_trudie():
    result = greet("Trudie")
    assert result == "Hello, Trudie!"