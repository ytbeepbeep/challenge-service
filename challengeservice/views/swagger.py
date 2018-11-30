import os
from flakon import SwaggerBlueprint
from flask import request, jsonify, abort, make_response
from challengeservice.database import db, Challenge

HERE = os.path.dirname(__file__)
YML = os.path.join(HERE, '..', 'static', 'api.yaml')
api = SwaggerBlueprint('API', __name__, swagger_spec=YML)


@api.operation('getChallenges')
def get_challenges():
    user_id = request.args.get('user_id')
    if not user_id:
        abort(400)
    challenges = db.session.query(Challenge).filter(Challenge.id_user == user_id)
    return jsonify([challenge.to_json() for challenge in challenges])


@api.operation('createChallenge')
def create_challenge():
    req = request.json
    challenge = Challenge()
    challenge.id_user = req['id_user']
    challenge.run_one = req['run_one']
    challenge.name_run_one = req['name_run_one']
    challenge.run_two = req['run_two']
    challenge.name_run_two = req['name_run_two']
    db.session.add(challenge)
    db.session.commit()
    return challenge.to_json()


@api.operation('getChallenge')
def get_challenge(challenge_id):
    challenge = db.session.query(Challenge).filter(Challenge.id == challenge_id).first()
    if not challenge:
        abort(404)
    return challenge.to_json()


@api.operation('deleteChallenges')
def delete_challenges():
    user_id = request.args.get('user_id')
    if not user_id:
        abort(400)
    challenges = db.session.query(Challenge).filter(Challenge.id_user == user_id).all()
    if not challenges:
        return abort(404)

    for c in challenges:
        db.session.delete(c)
    db.session.commit()
    return make_response('OK')
