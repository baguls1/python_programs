import pytest


def test_firstProgram():
    print('hello')

@pytest.mark.smoke
def test_second():
    print('world')