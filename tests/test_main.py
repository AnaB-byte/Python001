"""Tests for the main module."""

import pytest

from python001.main import hello


class TestHello:
    """Test cases for the hello function."""

    def test_hello_default(self) -> None:
        """Test hello with default argument."""
        assert hello() == "Hello, World!"

    def test_hello_custom(self) -> None:
        """Test hello with custom name."""
        assert hello("Alice") == "Hello, Alice!"
