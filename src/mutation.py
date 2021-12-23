import graphene
from .mutations.index import CreateUser, CreatePost, CreateRole


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    create_role = CreateRole.Field()
