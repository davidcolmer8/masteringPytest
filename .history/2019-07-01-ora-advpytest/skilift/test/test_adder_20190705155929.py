import adder

@pytest.mark.parmaetrize('x,y,z'[(2,2,)])
def test_add():
    res = adder.add(2,2)
    assert res == 4