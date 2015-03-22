from bottle import redirect, run, route, install
from bottle.ext.mongo import MongoPlugin

from bson.json_util import dumps

plugin = MongoPlugin(uri="mongodb://127.0.0.1", db="cosysnode", json_mongo=True)
install(plugin)

@route('/', method='GET')
def index(mongodb):
    return dumps(mongodb['collection'].find())

@route('/api', method='GET')
def get_api(mongodb):
  return "OK"

@route('/create', method='POST')
def create(mongodb):
    mongodb['collection'].insert({'a': 1, 'b': 2})
    redirect("/")

run(host='localhost', port=5000)
