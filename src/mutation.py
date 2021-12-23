import graphene
from .mutations.index import (
    CreateUser,
    CreatePost,
    UpdatePost,
    DeletePost,
    CreateRole,
)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    create_role = CreateRole.Field()
