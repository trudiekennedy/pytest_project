from lib.counter import *

# Test checks that 1 number added correctly. 

def test_check_count_for_one_num():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

# Test checks that 2 numbers are correctly added together.

def test_check_count_for_2_nums():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 15 so far."

# Test checks 0 is returned if add not called

def test_check_count_no_number_given():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

# Tests if one of the numbers in negative

def test_check_count_neg_number_given():
    counter = Counter()
    counter.add(10)
    counter.add(-5)
    result = counter.report()
    assert result == "Counted to 5 so far."
