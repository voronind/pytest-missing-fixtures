import pytest
from pytest import fixture


# @fixture
# def a():
#     return 'a1'

# Need b fixture with function scope and tests/test_1.py baseid

# def test_base(b):
#     assert b == 'a1 b'


# @pytest.mark.usefixtures('b')
class TestCase:

    @fixture('class')
    def a(self):
        return 'a1'

    def test_method(self, b):
        # assert c == 'a b c'
        assert b == 'a1 b'