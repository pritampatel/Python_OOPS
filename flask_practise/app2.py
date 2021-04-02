from flask import Flask,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)
items=[]

class Item(Resource):
    def get(self,name):
        item=next(filter(lambda x: x['name']==name,items),None)
        return {'item':item,"status_code":200},200 if item else 400
    
    def post(self,name):
        if next(filter(lambda x: x['name']==name,items),None):
            return {'message':"An item with name already exists"},400 

        data= request.get_json()
        item= {"name":name,"price":data["price"]}
        items.append(item)
        return item,201 

class ItemList(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,"/itemlist")

if __name__=="__main__":
    app.run(port=5000)