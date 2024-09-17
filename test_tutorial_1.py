import pytest


def test_sample_one():
    print('this demo file')

@pytest.mark.smoke
def test_sample_sec():
    print("demo second")


def test_sample_third():
    print("demo third")


# rule to follow pytest

