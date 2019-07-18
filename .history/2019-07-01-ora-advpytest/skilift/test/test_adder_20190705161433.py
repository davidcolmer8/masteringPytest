import adder

import pytest

# @pytest.mark.parametrize('x,y,z',[(2,2,4)])
# def test_add(x,y,z):
#     res = adder.add(x,y)
#     assert res == z

@pytest.mark.parametrize('x')
def test_minus():
    res = adder.minus(2,2)
    assert res==0