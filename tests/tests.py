from unittest import mock

from starlette.testclient import TestClient
import pickledb

from bot import app

from utils import constants, message_utils

client = TestClient(app)


def test_message_post():
    message_utils.db = pickledb.load('fake.db', False)
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


def test_message_missing_values():
    response = client.post(
        '/message',
        json={
            "user_id": "fake",
        }
    )
    assert response.status_code == 422
    response = client.post(
        '/message',
        json={
            "message": "fake",
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
    response = client.post(
        '/message',
        '''{
            "user_id": ,
            "message": "fake",
        }'''
    )
    assert response.status_code == 400


def test_empty_history():
    response = client.get("/history")
    assert response.status_code == 422

def test_process_message():
    message_utils.db = pickledb.load('fake.db', False)
    message, finished = message_utils.process_message('fake', '/start')
    assert message == constants.question_tree['start']['message']
    assert not finished
    message, finished = message_utils.process_message('fake', 'да')
    assert message == constants.question_tree['square']['message']
