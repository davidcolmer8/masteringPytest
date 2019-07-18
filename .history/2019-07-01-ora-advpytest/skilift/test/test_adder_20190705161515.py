from pkg_resources import resource_exists

import adder
import pytest

# @pytest.mark.parametrize('x,y,z',[(2,2,4)])
# def test_add(x,y,z):
#     res = adder.add(x,y)
#     assert res == z

@pytest.mark.parametrize('a,b,result', [(3,3,0)])
def test_minus(a,b,result):
    res = adder.minus(a,b)
    assert res==0