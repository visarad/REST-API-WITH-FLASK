from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True,
                        help='This field cant be left blank')
    
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'Message':'Item Not found in dataBase'},400
        
    def post(self, name):
        
        if ItemModel.find_by_name(name):
            return {'message':'Item with Name {} already exists.'.format(name)},400
        
        data = Item.parser.parse_args()
        
        item = ItemModel(name, data['price'])
        
        try:
            item.insert()
        except:
            return {'message':'An Error Occured'}, 500
        
        return item.json() , 201
        
    
    def delete(self, name):
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'DELETE FROM  items WHERE name=?'
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {"Message": "Item Deleted "}
    
    
    def put(self, name):
        
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {'Message':"An Error occured during Insertion"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {'Message': "An Error occured during update"}, 500
        return updated_item.json()



class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
    
        query = "select * from items"
        result = cursor.execute(query)
    
        rows = result.fetchall()
        connection.close()
        items = []
        for row in rows:
           item =  {'name': row[0], 'price': row[1]}
           items.append(item)
        return  {'items':items}