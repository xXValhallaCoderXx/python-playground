from flask import request, json, jsonify, Blueprint, Response
from ..models.todo import Todo, TodoSchema

todo_api = Blueprint('todos', __name__)
todo_schema = TodoSchema()

@todo_api.route("/", methods=["POST", "GET"])
def todos():

  if request.method == "POST":
    req_data = request.get_json()
    data, error = todo_schema.load(req_data)

    if error:
      return custom_response(error, 400)

    todo = Todo(data)
    todo.save()
    todo_data = todo_schema.dump(todo).data
    return custom_response({'todo': todo_data, "success": True}, 200)

  else:
      todos = Todo.get_all_todos()
      todo_data = todo_schema.dump(todos, many=True).data

      return custom_response({'todos': todo_data, "success": True}, 200)
  

@todo_api.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
def todo_manipulate(id):
  todo = Todo.get_one_todo(id)

  if not todo:
    return custom_response({"todos": None, "success": True}, 404)
  
  if request.method == "GET":
    todo_data = todo_schema.dump(todo).data
    return custom_response({'todo': todo_data, "success": True}, 200)
  
  if request.method == "DELETE":
    todo_data = todo_schema.dump(todo).data
    todo.delete()
    return custom_response({'todo': todo_data, "success": True}, 200)

  if request.method == "PUT":
    req_data = request.get_json()

    data, error = todo_schema.load(req_data, partial=True)
    if error:
      return custom_response(error, 400)
    
    todo.update(req_data)
    todo_data = todo_schema.dump(todo).data

    return custom_response({'todo': todo_data, "success": True}, 200)
  


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )