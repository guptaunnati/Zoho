import pytest

def findSum(num1, num2):
    return num1+num2

@pytest.mark.parametrize('num1, num2, expected', [(3, 1, 4), (4, 5, 9), (7, 8, 15)])
def test_sum(num1, num2, expected):
    assert num1+num2==expected

@pytest.mark.parametrize('num1, num2, expected', [(3, 1, 4), (4, 5, 9), (7, 8, 15)])
def test_findSum(num1, num2, expected):
    assert findSum(num1, num2)==expected
