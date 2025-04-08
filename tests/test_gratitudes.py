from lib.gratitudes import *

# Tests that nothing returned if nothing passed into add

def test_gratitudes_not_added():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "

# Tests what happens when one gratitude is passed

def test_gratitudes_one_added():
    gratitudes = Gratitudes()
    gratitudes.add("friends")
    result = gratitudes.format()
    assert result == "Be grateful for: friends"

# Tests what happens when more than one gratitudes are added

def test_gratitudes_more_than_one():
    gratitudes = Gratitudes()
    gratitudes.add("friends")
    gratitudes.add("family")
    gratitudes.add("fun shenanigans")
    result = gratitudes.format()
    assert result == "Be grateful for: friends, family, fun shenanigans"