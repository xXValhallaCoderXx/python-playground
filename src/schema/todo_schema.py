from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.todo import Todo as TodoModel
import graphene


# Create a generic class to mutualize description of people attributes for both queries and mutations
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



def input_to_dictionary(input):
    """Method to convert Graphene inputs into dictionary."""
    dictionary = {}
    for key in input:
        # Convert GraphQL global id to database id
        if key[-2:] == 'id' and input[key] != 'unknown':
            input[key] = from_global_id(input[key])[1]
        dictionary[key] = input[key]
    return dictionary