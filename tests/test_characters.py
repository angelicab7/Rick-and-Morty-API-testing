import requests

base_url = "https://rickandmortyapi.com/api"
character_id = 2
name = "rick"
status = "alive"

def test_get_characters_healthcheck():
    response = requests.get(base_url + "/character/") 
    assert response.status_code == 200
    pass
    
def test_get_single_character():
    response = requests.get(base_url + "/character/{}".format(character_id))
    assert response.status_code == 200
    assert response.json()["id"] == character_id
    print(response.json())
    pass

def test_get_multiple_characters():
    response = requests.get(base_url + "/character/".format([1,2,3]))
    assert response.status_code == 200
    pass

def test_filter_characters():
     response = requests.get(base_url + "/character/?" + "name=" + name + "&status=" + status)
     assert response.status_code == 200
     pass

