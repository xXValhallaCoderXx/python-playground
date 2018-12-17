import graphene
from .todo_schema import CreateTodo


class Mutations(graphene.ObjectType):
    create_todo = CreateTodo.Field()