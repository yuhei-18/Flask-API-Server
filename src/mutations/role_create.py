import graphene
from ..models.index import Role as RoleModel
from ..objects.index import Role


class CreateRoleInput(graphene.InputObjectType):
    """
    役割作成 Mutation 用の Input
    """
    name = graphene.String(
        description="役割の名前",
        requred=True
    )


class CreateRole(graphene.Mutation):
    """
    役割の作成 Mutation
    """
    role = graphene.Field(Role)

    class Arguments:
        input = CreateRoleInput()

    @staticmethod
    def mutate(root, info, input):
        role = RoleModel(name=input.name)
        role.save()
        return CreateRole(role=role)
