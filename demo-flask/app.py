from flask import Flask, Response, jsonify, request
import database_services.RDBService as d_service
import json
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.UsersResource.user_service import UserResource
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'
# @app.route('/User')
# def get_users():
#     res = UserResource.get_by_template(None)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp
@app.route('/User/ID/<id>')
def get_by_id(id):
    res=UserResource.get_by_user_id(id)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp
@app.route('/User/nameLast/<nameLast>')
def get_by_lastname(nameLast):
    res=UserResource.get_by_lastname(nameLast)
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
    UserResource.get_by_template()
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp
@app.route('/api/users/<id>', methods = ['DELETE'])
def delete_user_by_ID(id):
    res = UserResource.delete_by_user_id(id)
    rsp = Response(json.dumps(res, default=str), status=204, content_type="application/json")
    return rsp
@app.route('/api/users',methods=[ 'POST'])
def add_user_new():
    data= request.form
    res = UserResource.add_user(data['ID'], data['nameFirst'], data['nameLast'], data['email'], data['addressID'])
    print('add_new')
    rsp =Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp
@app.route('/api/users/<id>/address', methods = ['GET'])
def select_adress_by_user_ID(id):
    res = UserResource.select_adress_by_user_id(id)
    print(res)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp
@app.route('/api/users/change', methods=['POST'])
def update_user_by_ID():
    data = request.form
    print("11111")
    res = UserResource.update_by_user_id(data['ID'], data['email'])
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


# @app.errorhandler(404)
# def page_not_found(e):
#     return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
