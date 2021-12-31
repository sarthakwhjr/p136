from flask import Flask,jsonify,request
from projectdata import data
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"succesfull"
    }),200
@app.route("/stars") 
def planet():
    name=request.args.get("name")
    planetdata=next(i for i in data if i ["name"]==name)
    return jsonify({
        "data":planetdata,
        "message":"succesfull"
        }),200
if __name__=="__main__" :
    app.run()         
