from mongoengine.fields import StringField, EmailField, ReferenceField
from .base import BaseDocument, NULLIFY
from .role import Role


class User(BaseDocument):
    """
    ユーザー情報
    """
    meta = {"collection": "Users"}

    name = StringField(
        db_field="name",
        help_text="ユーザーの名前",
        requred=True
    )
    email = EmailField(
        db_field="email",
        help_text="ユーザーのメールアドレス",
        requred=True,
        unique=True
    )
    password = StringField(
        db_field="password",
        help_text="ユーザーのパスワード",
        requred=True
    )
    role = ReferenceField(
        Role, reverse_delete_rule=NULLIFY,
        db_field="role",
        help_text="ユーザーの役割"
    )
