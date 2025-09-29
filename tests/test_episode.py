import requests

base_url = "https://rickandmortyapi.com/api"
episode_id = 28
episode_name = "Pilot"


def test_get_episode_healthcheck():
    response = requests.get(base_url + "/episode") 
    assert response.status_code == 200
    pass

def test_get_single_episode():
    response = requests.get(base_url + "/episode/{}".format(episode_id))
    assert response.status_code == 200
    assert response.json()["id"] == episode_id
    print(response.json())
    pass

def test_get_multiple_episode():
    response = requests.get(base_url + "/episode/".format([1,7,30]))
    assert response.status_code == 200
    pass

def test_filter_episode():
     response = requests.get(base_url + "/episode?name=" + episode_name)
     assert response.status_code == 200
     pass