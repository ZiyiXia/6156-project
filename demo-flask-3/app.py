from flask import Flask, Response, jsonify, request
import database_services.RDBService as d_service
import json
import logging
from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.UsersResource.user_service import UserResource

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/player/idPlayer/<id>')
def get_by_id(id):
    res = UserResource.get_by_player_id(id)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/player/Name/<Name>')
def get_by_name(name):
    res = UserResource.get_by_name(name)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/player/Nationality/<Nationality>')
def get_by_nationality(nationality):
    res = UserResource.get_by_nationality(nationality)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/api/players/<id>', methods=['DELETE'])
def delete_player_by_id(id):
    res = UserResource.delete_by_player_id(id)
    rsp = Response(json.dumps(res, default=str), status=204, content_type="application/json")
    return rsp


@app.route('/api/players', methods=['POST'])
def add_user_new():
    data = request.form
    res = UserResource.add_player(data['idPlayer'], data['Name'], data['Nationality'], data['idClub'])
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/api/players/<id>/club', methods=['GET'])
def select_club_by_player_id(id):
    res = UserResource.select_club_by_player_id(id)
    print(res)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/api/players/change', methods=['POST'])
def update_player_by_id():
    data = request.form
    res = UserResource.update_by_player_id(data['playerID'], data['name'])
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


# @app.route('/players')
# def get_players():
#     res = UserResource.get_by_player_template(None)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp
#
#
# @app.route('/players', methods=['POST'])
# def put_players():
#     data = request.form
#
#     res = UserResource.put_by_player_template(None, data['ID'], data['name'])
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp
#
#
# @app.route('/club')
# def get_club():
#     res = UserResource.get_by_club_template(None)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = d_service.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/users/<prefix>')
def get_users_by_prefix(prefix):
    res = UserResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
