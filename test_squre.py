import pytest
import requests
import json

# @pytest.fixture
# def main_url():
#     return 'https://reqres.in'
    
# def test_valid_login(main_url):
#     url = main_url +"/api/login"
#     data = {'email':'eve.holt@reqres.i','password':'cityslicka'}
#     response = requests.post(url,data=data)
#     t = json.loads(response.text)
#     assert response.status_code ==200
#     assert t['token']== "QpwL5tke4Pnpja7X4"

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
    
    

