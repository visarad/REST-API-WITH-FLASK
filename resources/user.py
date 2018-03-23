import sqlite3
from flask_restful import Resource
from flask_restful import reqparse
from models.user import UserModel


class UserRegister(Resource):
    parsor = reqparse.RequestParser()
    parsor.add_argument('username',type=str, required=True,
                        help='This field cant be blank')
    parsor.add_argument('password',type=str, required=True,
                        help='This field cant be blank')
        
    def post(self):
        data = UserRegister.parsor.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message':"A User With the name exists"}, 400
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(query, (data['username'],data['password']))
        connection.commit()
        connection.close()
        return {'Message':'User creatd successfully'}, 201
