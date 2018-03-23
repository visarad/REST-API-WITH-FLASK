from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'it is that secrete ?.'
api = Api(app)

jwt = JWT(app,authenticate,identity)

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList,  '/items')
api.add_resource(UserRegister,  '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)


