from currencies import convert
from nose.tools import eq_

def test_convert_usd_to_eur():
    amount = (100, "USD")
    result = convert(amount, "EUR")
    eq_(85, result)

def test_convert_chf_to_eur():
    amount = (200, "CHF")
    result = convert(amount, "EUR")
    eq_(172, result)

def test_convert_gbp_to_eur():
    amount = (300, "GBP")
    result = convert(amount, "EUR")
    eq_(339, result)

def test_should_handle_a_missing_rate():
    amount = (300, "RMB")
    result = convert(amount, "EUR")
    eq_(None, result)
