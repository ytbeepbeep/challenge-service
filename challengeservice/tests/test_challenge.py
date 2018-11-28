from challengeservice.tests.utility import client, new_challenge
from challengeservice.database import db, Challenge 
import requests
import requests_mock


def test_create_challenge(client):
    tested_app, app = client

    challenge1 = new_challenge()
    json = challenge1.to_json()

    # inserting a challenge
    assert tested_app.post('/challenges', json=json).status_code == 200

    # checking the correct insertion
    with app.app_context():
        challenge = db.session.query(Challenge).filter(challenge1.id_user == Challenge.id_user).first()
        assert challenge.run_one == challenge1.run_one
        assert challenge.name_run_one == challenge1.name_run_one
        assert challenge.run_two == challenge1.run_two
        assert challenge.name_run_two == challenge1.name_run_two

    assert tested_app.get('/challenges/50').status_code == 404
    assert tested_app.get('/challenges/1').status_code == 200