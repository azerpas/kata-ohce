import pytest

from ohce.greeter import Greeter

class MockClock:
    def __init__(self) -> None:
        self.hour = 0

    def set_current_hour(self, hour):
        self.hour = hour

    def current_hour(self):
        return self.hour

def test_nightly_greeting():
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    g = Greeter(MockClock)
    assert g.greet() == "Good night"

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
