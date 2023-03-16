import pytest
import requests
 

def test_status_code():
    url = ("https://reqres.in/api/users/2")
    response = requests.get(url)
    assert response.status_code == 200


def test_resourсе_not_found():
    url = ("https://reqres.in/api/unknown/23")
    response = requests.get(url)
    assert response.status_code == 404


def test_check_response():
    url = ("https://reqres.in/api/users/2")
    response = requests.get(url)
    response = response.json()['data']
    assert response["first_name"] == "Janet"


 
data = [("name", "cerulean", 1, 0),("color", "#C74375", 2, 1),("year", 2002 , 3, 2)]

@pytest.mark.parametrize("key, value, id, row", data)
def test_part_of_body(key, value, id, row):
    url = f"https://reqres.in/api/unknown{id}"
    response = requests.get(url)
    response = response.json()["data"]
    assert response[row][key] == value

    