from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

todos = {}

def abort_if_not_exists(todo_id):
    if todo_id not in todos:
        abort(404)

class TodoSimple(Resource):
    def get(self, todo_id):
        abort_if_not_exists(todo_id)
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        abort_if_not_exists(todo_id)
        del todos[todo_id]
        return " ", 204

api.add_resource(TodoSimple, '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)