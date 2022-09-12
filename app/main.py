from mangum import Mangum
from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry

from schema import Query

schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()


@app.get('/')
def ping():
    return {'ping': 'pong'}


app.add_route("/gql", graphql_app)
app.add_websocket_route("/gql", graphql_app)

handler = Mangum(app)
