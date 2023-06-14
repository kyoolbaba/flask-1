from flask import Flask, request
from flask_restful import Api,Resource,reqparse
from sqlconstruct.add_hey import add_key;
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
api=Api(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tmp/database.db"
# db=SQLAlchemy()
# class VideoModel(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(255),nullable=False)
#     views=db.Column(db.Integer,nullable=False)
#     likes=db.Column(db.Integer,nullable=False)

#     def __repe__(self):
#         return f''' id={id} , name={name} , likes={likes}'''
# db.create_all()



class Hello_world(Resource):
    def get(self):
        return {"name":"HEllo world"}  
    def post(self):
        return {"name":"HEllo world From POst"} 
    
class Greeting(Resource):
    def get(self,name):
        return {"name":f''' Hey This is {name} '''}
    
class giveBioData(Resource):
    def get(self,name=None,age=None,location=None):
        # return add_key("MILAN")     
        return {"name":name,"age":age,"location":location}
api.add_resource(Hello_world,'/hello_world') 
api.add_resource(Greeting,'/greet/<string:name>') 
api.add_resource(giveBioData,'/biodata/<string:name>/<int:age>/<string:location>') 
# profile=reqparse.RequestParser()
# profile.add_argument("name",required=True,type=str,help="Enter the ID")
# profile.add_argument("age",required=True,type=int,help="Enter the Age")
# profile.add_argument("likes",required=True,type=int,help="Enter the Age")
# profile.add_argument("views",required=True,type=int,help="Enter the Age")



@app.route('/inputjson', methods=['POST'])
def inputjson():
    req_data=request.get_json()
    result=add_key("",req_data)
    return result



if __name__=="__main__":
    app.run(debug=True)