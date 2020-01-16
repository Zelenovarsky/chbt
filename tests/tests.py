from starlette.testclient import TestClient

from bot import app

client = TestClient(app)


def test_message_post():
    response = client.post(
        '/message',
        json={
            "user_id": "fake",
            "message": "fake",
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        "чтобы начать, напишите /start",
        0
    ]

def test_check_message():
    answer_mapping = {
        {'ага', 'да', 'конечно', 'пожалуй', 'ес', 'угу'}
    }

def test_message_missing_values():
    response = client.post(
        '/message',
        json={
              "user_id": "fake",
        }
    )
    assert response.status_code == 422


def test_message_bad_request():
    response = client.post(
        '/message',
        '''{
            "user_id": "fake",
            "message": ,
        }'''
    )
    assert response.status_code == 400


def test_empty_history():
    response = client.get("/history")
    assert response.status_code == 422

