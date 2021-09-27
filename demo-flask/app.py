from flask import Flask, Response
import database_services.RDBService as d_service
from flask_cors import CORS
import json

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.UsersResource.user_service import UserResource


app = Flask(__name__)
CORS(app)




@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/imdb/artists/<prefix>')
def get_artists_by_prefix(prefix):
    res = IMDBArtistResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/users')
def get_users():
    res = UserResource.get_by_template(None)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = d_service.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

@app.route('/users/<prefix>')
def get_users_by_prefix(prefix):
    res = UserResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
