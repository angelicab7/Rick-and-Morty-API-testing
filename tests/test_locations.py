import requests

base_url = "https://rickandmortyapi.com/api"
location_id = 3
location_type = "planet"

def test_get_locations_healthcheck():
    response = requests.get(base_url + "/location") 
    assert response.status_code == 200
    pass

def test_get_single_location():
    response = requests.get(base_url + "/location/{}".format(location_id))
    assert response.status_code == 200
    assert response.json()["id"] == location_id
    print(response.json())
    pass

def test_get_multiple_locations():
    response = requests.get(base_url + "/location".format([3,2,1]))
    assert response.status_code == 200
    pass

def test_filter_locations():
     response = requests.get(base_url + "/location?type=" + location_type)
     assert response.status_code == 200
     pass