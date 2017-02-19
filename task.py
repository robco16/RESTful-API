from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Task(Resource):
    TABLE_NAME = 'tasks'

    parser = reqparse.RequestParser()
    parser.add_argument('description',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        task = self.find_by_name(name)
        if task:
            return task
        return {'message': 'Task not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'task': {'name': row[0], 'description': row[1]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "A task with name '{}' already exists.".format(name)}

        data = Task.parser.parse_args()

        task = {'name': name, 'description': data['description']}

        try:
            Task.insert(task)
        except:
            return {"message": "An error occurred inserting the task."}

        return task

    @classmethod
    def insert(cls, task):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (task['name'], task['description']))

        connection.commit()
        connection.close()

    @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Task deleted'}

    @jwt_required()
    def put(self, name):
        data = Task.parser.parse_args()
        task = self.find_by_name(name)
        updated_item = {'name': name, 'description': data['description']}
        if task is None:
            try:
                Task.insert(updated_task)
            except:
                return {"message": "An error occurred inserting the task."}
        else:
            try:
                Task.update(updated_task)
            except:
                raise
                return {"message": "The task was not able to be updated."}
        return updated_task

    @classmethod
    def update(cls, task):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET description=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (task['description'], task['name']))

        connection.commit()
        connection.close()


class TaskList(Resource):
    TABLE_NAME = 'tasks'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        tasks = []
        for row in result:
            tasks.append({'name': row[0], 'description': row[1]})
        connection.close()

        return {'tasks': tasks}
