from challengeservice.tests.utility import client, new_challenge
from challengeservice.database import db, Challenge 
import requests
import requests_mock
import json


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

def test_get_challenge(client):
	tested_app, app = client

	challenge1 = new_challenge()
	json1 = challenge1.to_json()
	tested_app.post('/challenges', json=json1)
	
	assert tested_app.get('/challenges/50').status_code == 404

	challenge = tested_app.get('/challenges/1')
	assert challenge.status_code == 200

	challenge_json = json.loads(str(challenge.data, 'utf8'))
	with app.app_context():
		expected = db.session.query(Challenge).filter(challenge1.id_user == Challenge.id_user).first()
		assert expected.run_one == challenge_json['run_one']
		assert expected.name_run_one == challenge_json['name_run_one']
		assert expected.run_two == challenge_json['run_two']
		assert expected.name_run_two == challenge_json['name_run_two']

def test_get_multiple_challenges(client):
	tested_app, app = client

	challenge1 = new_challenge()
	challenge2 = new_challenge()
	challenge3 = new_challenge()
	json1 = challenge1.to_json()
	json2 = challenge2.to_json()
	json3 = challenge3.to_json()
	tested_app.post('/challenges', json=json1)
	tested_app.post('/challenges', json=json2)
	tested_app.post('/challenges', json=json3)

	challenges = tested_app.get('/challenges?user_id='+repr(challenge1.id_user))
	challenges_json = json.loads(str(challenges.data, 'utf8'))
	assert challenges.status_code == 200
	expected = [{'id': 1,
	'id_user': 1,
	'name_run_one': 'run_one',
	'name_run_two': 'run_two',
	'run_one': 1,
	'run_two': 2},
	{'id': 2,
	'id_user': 1,
	'name_run_one': 'run_one',
	'name_run_two': 'run_two',
	'run_one': 1,
	'run_two': 2},
	{'id': 3,
	'id_user': 1,
	'name_run_one': 'run_one',
	'name_run_two': 'run_two',
	'run_one': 1,
	'run_two': 2}]

	assert challenges_json == expected
	c = [challenge1, challenge2, challenge3]
	j = [json1, json2, json3]
	with app.app_context():
		for i, challenge in enumerate(c):
			expected = db.session.query(Challenge).filter(challenge.id_user == Challenge.id_user).first()
			assert expected.run_one == j[i]['run_one']
			assert expected.name_run_one == j[i]['name_run_one']
			assert expected.run_two == j[i]['run_two']
			assert expected.name_run_two == j[i]['name_run_two']

def test_delete_user(client):
	tested_app, app = client

	challenge1 = new_challenge()
	challenge2 = new_challenge()
	challenge3 = new_challenge()
	json1 = challenge1.to_json()
	json2 = challenge2.to_json()
	json3 = challenge3.to_json()

	assert tested_app.delete('/challenges?user_id='+repr(challenge1.id_user)).status_code == 404

	tested_app.post('/challenges', json=json1)
	tested_app.post('/challenges', json=json2)
	tested_app.post('/challenges', json=json3)

	assert tested_app.delete('/challenges?user_id='+repr(challenge1.id_user)).status_code == 200
	with app.app_context():
		expected = db.session.query(Challenge).filter(challenge1.id_user == Challenge.id_user).first()
		assert expected == None


