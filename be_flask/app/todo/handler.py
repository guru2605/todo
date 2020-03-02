from re import escape

from bson import ObjectId
from flask import current_app

from app.db import get_db


class TodoHandler:
    def __init__(self):
        self.db = get_db()

    def get_todo(self, data):
        """
        This method Get todo_list if the id is None else returns the matched_todo
        :param data:
        """
        todo_id = data.get('todo_id')
        skip = data.get('skip', 0)
        limit = data.get('limit', 10)
        pipeline = [
            {
                '$match': {
                    '_id': ObjectId(todo_id) if todo_id else {'$exists': True}
                }
            },
            {'$skip': skip},
            {'$limit': limit}
        ]
        todo_list = list(self.db.aggregate_docs(current_app.config['MONGO_DBNAME'], current_app.config['MONGO_COL_TODO'],
                                             pipeline))
        total = len(
            list(self.db.aggregate_docs(current_app.config['MONGO_DBNAME'], current_app.config['MONGO_COL_TODO'],
                                        pipeline[:-2])))
        return {'status_id': 1, 'todo_list': todo_list, 'total': total, 'filters': data}

    def store_todo(self, data):
        """
        This method creates a todo
        """
        title = data.get('title')
        description = data.get('description')

        if None in [title, description]:
            return {'status_id': 0, 'reason': 'Fill in required Fields'}

        todo = {
            'title': title,
            'description': description
        }
        res = self.db.insert_doc(todo, current_app.config['MONGO_DBNAME'], current_app.config['MONGO_COL_TODO'])

        if res.inserted_id:
            return {'status_id': 1, 'message': 'Todo Created Successfully!'}
        else:
            return {'status_id': 0, 'reason': 'Cannot Create Todo!'}

    def update_todo(self, data):
        """
        This method updates a todo using its id
        """
        todo_id = data.get('todo_id')
        title = data.get('title')
        description = data.get('description')

        if None in [title, description, todo_id]:
            return {'status_id': 0, 'reason': 'Fill in required Fields'}

        todo = {
            'title': title,
            'description': description
        }
        query = {
            '_id': ObjectId(todo_id)
        }
        res = self.db.update_one_doc(query, todo, current_app.config['MONGO_DBNAME'], current_app.config['MONGO_COL_TODO'])

        if res.modified_count:
            return {'status_id': 1, 'message': 'Todo Updated Successfully!'}
        else:
            return {'status_id': 0, 'reason': 'Cannot Update Todo!'}

    def delete_todo(self, todo_id):
        """
        This method deletes a todo using its id
        :param todo_id;
        """
        if None in [todo_id]:
            return {'status_id': 0, 'reason': 'Bad Request!'}

        query = {
            '_id': ObjectId(todo_id)
        }
        res = self.db.delete_one_doc(current_app.config['MONGO_DBNAME'], current_app.config['MONGO_COL_TODO'], query)

        if res:
            return {'status_id': 1, 'message': 'Todo Deleted Successfully!'}
        else:
            return {'status_id': 0, 'reason': 'Cannot Delete Todo!'}
