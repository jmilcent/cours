from nose.tools import eq_
from sum_of_three import sum3

def test_numbers_0_0_0():
    eq_(sum3(0, 0, 0), 0)

def test_numbers_1_2_3():
    eq_(sum3(1, 2, 3), 6)

def test_with_negative_numbers():
    eq_(sum3(-1, 1, 0), 0)
