import pytest
from pytest import raises

from src import AlwaysAuthorized, SafeCalculator, NeverAuthorized
from src.unauthorized_access_exception import UnauthorizedAccessException


def test_add_should_not_raise_any_error_when_authorized():
    # Arrange
    authorizer = AlwaysAuthorized()
    safe_calculator = SafeCalculator(authorizer)

    # Act
    result = safe_calculator.add(1, 2)

    # Assert
    assert 3 == result


def test_add_should_raise_an_error_when_unauthorized():
    # Arrange
    authorizer = NeverAuthorized()
    safe_calculator = SafeCalculator(authorizer)

    # Act and Assert/Raise
    with raises(UnauthorizedAccessException, match='Not authorized'):
        safe_calculator.add(1, 2)
