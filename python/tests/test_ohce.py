import pytest

from ohce.greeter import Greeter


def test_nightly_greeting():
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    g = Greeter()
    g.clock.current_hour = lambda: 0
    assert g.greet() == "Good night"
    # TODO: use a clock mock instead of lambda


def test_greeting_never_returns_none():
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    pytest.fail("TODO")


def test_ohce_main_loop():
    """
    Given the following inputs:
    - hello
    - oto
    - quit

    Check that the following messages are printed:
    - olleh
    - oto
    - That was a palindrome!
    """
    pytest.fail("TODO")
