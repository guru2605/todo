from flask import Blueprint, jsonify, request
from .handler import TodoHandler


todo = Blueprint('todo', __name__)


@todo.route('/get', methods=["POST"])
def get_all_todo():
    return jsonify(TodoHandler().get_todo(request.json))


@todo.route('/create', methods=["POST"])
def store_todo():
    return jsonify(TodoHandler().store_todo(request.json))


@todo.route('/update', methods=["POST"])
def update_todo():
    return jsonify(TodoHandler().update_todo(request.json))


@todo.route('/delete', methods=["POST"])
def delete_todo():
    return jsonify(TodoHandler().delete_todo(request.json.get('todo_id')))



