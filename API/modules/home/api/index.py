from flask import jsonify,request
from modules.home import home_bp 
from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return jsonify({'message':'Online Complaint Management System'}) 
    
    def post(self):
        data = request.get_json() 
        return jsonify({'data':data})