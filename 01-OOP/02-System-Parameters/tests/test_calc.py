from calc import main
from nose.tools import eq_
import sys

def test_4_plus_5():
    sys.argv = [ "", "4", "+", "5"]
    eq_(main(), 9)

def test_2_times_6():
    sys.argv = [ "", "2", "*", "6"]
    eq_(main(), 12)

def test_3_minus_9():
    sys.argv = [ "", "3", "-", "9"]
    eq_(main(), -6)
