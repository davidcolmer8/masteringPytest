import adder

import pytest

@pytest.mark.parmaetrize('x,y,z',[(2,2,4)])
def test_add(x,y,z):
    res = adder.add(x,y)
    assert res == z