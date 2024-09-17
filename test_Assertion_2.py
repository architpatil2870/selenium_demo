import pytest


def test_sampple():
    a = 45
    b = 75
    assert a < b  # Correct assertion based on values
    print('this gretest than a')

@pytest.mark.smoke
def test_sampplew():
    a = 78
    b = 75
    assert a > b  # Correct assertion based on values
