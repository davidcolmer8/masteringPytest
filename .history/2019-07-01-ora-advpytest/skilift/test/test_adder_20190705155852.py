import adder

@pytest
def test_add():
    res = adder.add(2,2)
    assert res == 4