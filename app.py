import os
import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from mongoengine import connect
from src.query import Query
from src.mutation import Mutation
from src.objects.index import User, Post, Role

DATABASE = os.environ.get("MONGODB_DATABASE")
PASSWORD = os.environ.get("MONGODB_PASSWORD")
USER = os.environ.get("MONGODB_USER")

client = connect(
    DATABASE,
    host=f'mongodb+srv://{USER}:{PASSWORD}@cluster0.0nkk6.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE',
    alias='default'
)
schema = graphene.Schema(query=Query, mutation=Mutation, types=[User, Post, Role])
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)
CORS(app, origins=["http://localhost:8000"])


@app.route('/')
def index():
    return "Connect Success !!"

if __name__ == "__main__":
    app.run(debug=True)
