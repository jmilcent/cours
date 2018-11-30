# pylint: disable=missing-docstring

from nose.tools import eq_

from string_methods import add_comma
from string_methods import belongs_to
from string_methods import count_repetition
from string_methods import is_a_question
from string_methods import replace
from string_methods import remove_surrounding_whitespaces
from string_methods import full_description_concatenation
from string_methods import full_description_formatting


# add_comma

def test_strings_boris_romain_seb():
    """This method should return "boris, romain, seb" """
    eq_(add_comma("boris romain seb"), "boris, romain, seb")

def test_strings_boris_seb_romain():
    """This method should return "boris, seb, romain" """
    eq_(add_comma("boris seb romain"), "boris, seb, romain")


# belongs_to

def test_include_word():
    """This method should return True as 'hey jude' contains 'jude'"""
    eq_(belongs_to("hey jude", "jude"), True)

def test_do_not_include_word():
    """This method should return False as 'hey jude' doesn't contain 'joe'"""
    eq_(belongs_to("hey jude", "joe"), False)


# count_repetition

def test_numbers_0_0_1_2_0_on_0():
    """This method should return 3"""
    eq_(count_repetition("00120", "0"), 3)

def test_numbers_0_0_1_2_0_on_3():
    """This method should return 0 if a_substring doesn't occur in a_string"""
    eq_(count_repetition("00120", "3"), 0)


# is_a_question

def test_is_a_question():
    """This method should return True when a_string ends with a '?'"""
    eq_(is_a_question("How are you?"), True)

def test_is_not_a_question():
    """This method should return False when a_string doesn't end with a '?'"""
    eq_(is_a_question("Fine."), False)


#delete_surrounding_whitespaces

def test_leading_whitespaces():
    """This method should work with leading whitespaces"""
    eq_(remove_surrounding_whitespaces("  hey yo"), "hey yo")

def test_trailing_whitespaces():
    """This method should work with trailing whitespaces"""
    eq_(remove_surrounding_whitespaces("hey yo  "), "hey yo")

def test_whitespaces():
    """This method should work with leading and trailing whitespaces"""
    eq_(remove_surrounding_whitespaces(" hey yo  "), "hey yo")


# replace

def test_casanova_to_cosonovo():
    """This method should correctly replace the letter(s) in the string"""
    eq_(replace("casanova", "a", "o"), "cosonovo")

def test_kosovo_to_kasava():
    """This method should correctly replace the letter(s) in the string"""
    eq_(replace("kosovo", "o", "a"), "kasava")


# full_description_concatenation

def test_john_doe_33_concatenation():
    """This method should correctly return the full name and the age"""
    eq_(full_description_concatenation("John", "Doe", 33), "John Doe is 33")


# full_description_formatting

def test_john_doe_33_formatting():
    """This method should correctly return the full name and the age"""
    eq_(full_description_formatting("John", "Doe", 33), "John Doe is 33")
