from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from task import Task, TaskList

app = Flask(__name__)
app.secret_key = 'ig95db96rc97'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Task, '/task/<string:name>')
api.add_resource(TaskList, '/tasks')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
