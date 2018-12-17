import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .todo_schema import CreateTodo, UpdateTodo, Todo

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    todo = graphene.relay.Node.Field(Todo)
    todos = SQLAlchemyConnectionField(Todo)


class Mutations(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)