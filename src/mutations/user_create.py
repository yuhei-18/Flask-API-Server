import graphene
from ..models.index import User as UserModel, Role
from ..objects.index import User


class CreateUserInput(graphene.InputObjectType):
    """
    ユーザー作成 Mutation 用の Input
    """
    name = graphene.String(
        description="ユーザーの名前",
        requred=True
    )
    email = graphene.String(
        description="ユーザーのメールアドレス",
        requred=True
    )
    password = graphene.String(
        description="ユーザーのパスワード",
        requred=True
    )
    role = graphene.String(
        description="ユーザーの役割"
    )


class CreateUser(graphene.Mutation):
    """
    ユーザー作成 Mutation
    """
    user = graphene.Field(User)

    class Arguments:
        input = CreateUserInput()

    @staticmethod
    def mutate(root, info, input):
        role = Role.objects.get(name=input.role)
        user = UserModel(
            name=input.name,
            email=input.email,
            password=input.password,
            role=role
        )
        user.save()
        return CreateUser(user=user)
