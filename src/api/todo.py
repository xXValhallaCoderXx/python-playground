from flask import request, json, jsonify, Blueprint
from ..models.todo import Todo

todo_api = Blueprint('todos', __name__)

@todo_api.route("/", methods=["POST", "GET"])
def todos():

  if request.method == "POST":
    req_data = request.get_json()
    text = req_data['text']
    try:

      new_todo = Todo(text=text)
      new_todo.save()

      response = jsonify({
        "success": True,
        "data": {
          "text": new_todo.text,
          "completed": new_todo.completed,
          "id": new_todo.id
        }
      })
      response.status_code = 200
    
    except Exception as e:
      print(e)
      response = jsonify({
        "success": False,
        "data": None
      })
      response.status_code = 400

    return response
  else:
    try:
      todos = Todo.get_all_todos()
      results = []

      for todo in todos:
        obj = {
          "id": todo.id,
          "text": todo.text,
          "completed": todo.completed,
          "created_at": todo.created_at
        }
        results.append(obj)

      response = jsonify({
        "success": True,
        "data": results
      })
      response.status_code = 200
  
    except Exception as e:
      response = jsonify({
        "success": False,
        "data": None
      })
      response.status_code = 400
  
  return response

@todo_api.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
def todo_manipulate(id):
  todo = Todo.get_one_todo(id)

  if not todo:
    response = jsonify({
      "success": False,
      "data": "ID not found"
    })
    response.status_code = 404
    return response
  
  if request.method == "GET":
    response = jsonify({
      "success": True,
      "data": {
        "text": todo.text,
        "completed": todo.completed,
        "id": todo.id
      }
    })
    response.status_code = 200
    return response
  
  if request.method == "DELETE":
    todo.delete()
    response = jsonify({
      "success": True,
      "data": {
        "text": todo.text,
        "completed": todo.completed,
        "id": todo.id
      }
    })
    response.status_code = 200
    return response

  if request.method == "PUT":
    req_data = request.get_json()
    todo.text = req_data['text']
    todo.completed = req_data['completed']
    todo.save()

    response = jsonify({
      "success": True,
      "data": {
        "text": todo.text,
        "completed": todo.completed,
        "id": todo.id
        }
      })
    response.status_code = 200
    return response
  