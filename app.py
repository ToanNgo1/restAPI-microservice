import requests
from flask import Flask,jsonify
app=Flask("sample")

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def get_empty_slot():
    return max(ct["id"] for ct in countries)+1      #return the next available slots for data

#root
def selector(dic,target):
    for i in dic:
        for key,value in i.items():
            if key=="id" and value==target:
                packet=i
                return packet
    return None
        
@app.route("/")
def root():
    return ("welcome to api test")

@app.route("/value",methods=['GET'])
def get_value():        #get all value
    return jsonify(countries),201

@app.route("/value/<id>",methods=["GET"])
def get_by_id(id):
    #print(id)
    packt=selector(countries,id)
    if(packt):
        return jsonify(packt),201
    else:
        return 404
    
#post request
@app.route("/countries",methods=['POST'])
def create_new():
    #check is request is json
    if requests.is_json:
        country=requests.get_json       #unpacket json object
        country["id"]=get_empty_slot()
        countries.append(country)
        return country,201
    else:
        message={"error":"please enter the request as a json format!"}
        return jsonify(message),415
    
@app.route(f"/remove",methods=['POST'])
def remove():
    if requests.is_json:
        d_id=requests.get_json
        #status=remove_data(d_id["id"])
       # if(status):
            #resucturte(countries)
        #    return 201
       # else:
       #     message={"error":"no matching id type"}
        #    return jsonify(message),404
    else:
        message={"error":"please enter the request as a json format!"}
        return jsonify(message),415
        