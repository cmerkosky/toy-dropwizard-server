import requests
import pytest # have to install via command "pip3 install -U pytest"

BASE_URL = 'http://localhost:8085'
HELLO_WORLD_URL = BASE_URL + "/hello-world"

def test_health_check():
    r = requests.get(BASE_URL)
    assert(r.status_code == 404)

# 1. Add two more tests here of your choice. I will explain the API.
#    Make sure to verify the necessary info, e.g., status code, response data.
# 2. Add "pytest" as integration testing script as part of Github Actions CI workflow (you've done this before!)

def test_id_counter():
    r1 = requests.get(HELLO_WORLD_URL)
    id1 = r1.json()['id']
    r2 = requests.get(HELLO_WORLD_URL)
    id2 = r2.json()['id']

    assert(r2.status_code == 200)
    assert(id2 == id1+1)

def test_hello_name():
    name = "Cole"
    r = requests.get(HELLO_WORLD_URL + "?name=" + name)

    assert(r.status_code == 200)
    assert(r.json()['content'] == "Hello, " + name + "!")