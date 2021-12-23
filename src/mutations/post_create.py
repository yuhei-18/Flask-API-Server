import graphene
from ..models.index import Post as PostModel, User
from ..objects.index import Post


class CreatePostInput(graphene.InputObjectType):
    """
    投稿作成 Mutation 用の Input
    """
    text = graphene.String(
        description="投稿の内容",
        requred=True
    )
    author_email = graphene.String(
        description="投稿者のメールアドレス",
        requred=True
    )
    is_publish = graphene.Boolean(
        description="投稿を公開するかのフラグ"
    )


class CreatePost(graphene.Mutation):
    """
    投稿作成 Mutation
    """
    post = graphene.Field(Post)

    class Arguments:
        input = CreatePostInput()

    @staticmethod
    def mutate(root, info, input):
        user = User.objects.get(email=input.author_email)
        post = PostModel(
            text=input.text,
            author=user,
            is_publish=input.is_publish
        )
        post.save()
        return CreatePost(post=post)
