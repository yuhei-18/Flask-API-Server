from mongoengine.fields import StringField
from .base import BaseDocument


class Role(BaseDocument):
    """
    ユーザーの役割情報
    """
    meta = {"collection": "Roles"}

    name = StringField(
        db_field="name",
        help_text="役割の名前",
        requred=True
    )
