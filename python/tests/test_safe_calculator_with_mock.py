from unittest.mock import Mock

import pytest
from pytest import raises

from src import SafeCalculator
from src.unauthorized_access_exception import UnauthorizedAccessException


def test_add_should_not_raise_any_error_when_authorized():
    # Arrange
    mock_authorizer = Mock()
    mock_authorizer.authorize.return_value = True
    safe_calculator = SafeCalculator(mock_authorizer)

    # Act
    result = safe_calculator.add(1, 2)

    # Assert
    assert result == 3


def test_add_should_raise_an_error_when_unauthorized():
    # Arrange
    mock_authorizer = Mock()
    mock_authorizer.authorize.return_value = False
    safe_calculator = SafeCalculator(mock_authorizer)

    # Act and Assert
    with raises(UnauthorizedAccessException, match='Not authorized'):
        safe_calculator.add(1, 2)
