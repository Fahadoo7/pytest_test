import pytest

@pytest.fixture
def numbers():
    a=10
    b=12
    c=22
    return [a,b,c]
def test1():
    a = numbers()
    z=10
    assert z==a[0]
    
def test2(numbers):
    z=12
    assert z==numbers[1]
    
def test3(numbers):
    z=22
    assert z==numbers[2]
    
    

