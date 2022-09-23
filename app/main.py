from mangum import Mangum
from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry

app = FastAPI()


@app.get('/')
def ping():
    return {'ping': 'pong'}


handler = Mangum(app)
