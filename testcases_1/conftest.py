import pytest


@pytest.fixture()
def test_setup(yeild=None):
    print('this is testing automation')
    yeild
    print('ok for now')
