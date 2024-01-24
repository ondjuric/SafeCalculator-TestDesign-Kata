import pytest
from pytest import raises

from src import SafeCalculator
from src.unauthorized_access_exception import UnauthorizedAccessException

# This is for a method where the blocking part is at the outside (top or bottom) of the method


def test_add_with_authorization_check_should_not_raise_any_error_when_authorized():
    assert 3 == SafeCalculator.add_with_authorization_check(1, 2, True)


def test_add_with_authorization_check_should_raise_an_error_when_unauthorized():
    with raises(UnauthorizedAccessException, match='Not authorized'):
        SafeCalculator.add_with_authorization_check(1, 2, False)
