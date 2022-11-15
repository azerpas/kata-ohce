import pytest

from ohce.greeter import Greeter
from ohce.ui import UI

import io
from contextlib import redirect_stdout

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
    g = Greeter(MockClock)
    for i in range(24):
        g.clock.set_current_hour(i)
        assert g.greet() is not None

class MockInteractor:
    def set_input(self, input):
        self.input = input

    def read_input(self):
        return self.input

    def print_message(self, message):
        print(message)
        self.input = "quit"

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
    ui = UI(MockInteractor)
    
    ui.interactor.set_input("hello")
    f = io.StringIO()
    with redirect_stdout(f):
        ui.main_loop()
    out = f.getvalue()
    assert "olleh" in out

    ui.interactor.set_input("oto")
    f = io.StringIO()
    with redirect_stdout(f):
        ui.main_loop()
    out = f.getvalue()
    assert "oto" in out
    assert "That was a palindrome!" in out

    
