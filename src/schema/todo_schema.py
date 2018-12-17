from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.todo import Todo as TodoModel
from ..utils import input_to_dictionary
from ..db import db_session
import graphene

class TodoAttribute:
    text = graphene.String(description="The description of the todo")


class Todo(SQLAlchemyObjectType, TodoAttribute):
    """Todo node."""

    class Meta:
        model = TodoModel
        interfaces = (graphene.relay.Node,)

class CreateTodoInput(graphene.InputObjectType, TodoAttribute):
    """Arguments to create a todo."""
    pass

class UpdateTodoInput(graphene.InputObjectType, TodoAttribute):
    """Arguments to update a todo."""
    id = graphene.ID(required=True, description="ID of Todo to update.")
  
class CreateTodo(graphene.Mutation):
  """Mutation to create Todo"""
  todo = graphene.Field(lambda: Todo, description="Create a todo")

  class Arguments:
    input = CreateTodoInput(required=True)
  
  def mutate(self, info, input):
    data = input_to_dictionary(input)
    todo = TodoModel(data)
    todo.save()
    return CreateTodo(todo=todo)

class UpdateTodo(graphene.Mutation):
    """Updates a todo"""
    todo = graphene.Field(lambda: Todo, description="Update the todo")

    class Arguments:
        input = UpdateTodoInput(required=True)
    
    def mutate(self, info, input):
        data = input_to_dictionary(input)
        
        todo = TodoModel.get_one_todo(id=data["id"])
        todo.update(data)
        todo = TodoModel.get_one_todo(id=data["id"])
        return UpdateTodo(todo=todo)