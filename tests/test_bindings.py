import pytest
import haddock_restraints


def test_example_function():
    result = haddock_restraints.example_function("test")
    assert "Processed: test" in result
