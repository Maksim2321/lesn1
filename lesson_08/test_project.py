import json
import pytest
import requests

bURL = "https://ru.yougile.com/"
token = ""
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

@pytest.fixture
def create_project():
    payload = {
        "title": "Test Project"
    }
    response = requests.post(bURL+'projects', json=payload, headers=headers)
    assert response.status_code == 201
    project_id = response.json()["id"]

    yield project_id

def test_positivProjectPost():
    payload = {
        "title": "New Project"
    }
    response = requests.post(bURL+'api-v2/projects', json=payload, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()

def test_negativeProjectPost():
    title = {
        "title" : ""
    }
    response = requests.post(bURL+'api-v2/projects', json=title, headers=headers)
    assert response.status_code == 400

def test_positivProjectGet(create_project):
   project_id = create_project

   response = requests.get(bURL+'projects/'+{project_id}, headers=headers)
   assert response.status_code == 200
   assert response.json()["id"] == project_id

def test_negativeProjectGet():
    response = requests.get(bURL+'projects/999999999')
    assert response.status_code == 404

def test_positivProjectPut(create_project):
    project_id = create_project
    payload = {
        "title": "Updated Project"
    }

    response = requests.put(bURL+'projects/',{project_id},json=payload,headers=headers)

    assert response.status_code == 200

def test_negativeProjectPut():
    payload = {
        "title": "Fail Update"
    }

    response = requests.put(bURL+'/projects/999999999',json=payload,headers=headers)

    assert response.status_code == 404