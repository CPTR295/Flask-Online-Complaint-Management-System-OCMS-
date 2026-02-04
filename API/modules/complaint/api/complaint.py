from flask import make_response,jsonify,request
from flask_restful import Resource

from main_cache import cache
from model.config import db_session
from model.db import Complaint
from modules.complaint.repository.complaint import ComplaintRepository

class ListComplaintRestAPI(Resource):
    @cache.memoize(timeout=50)
    def get(self):
        repo = ComplaintRepository(db_session)
        recs = repo.select_all()
        rec = [rec.to_json() for rec in recs]
        return make_response(jsonify(rec),200)

class AddComplaintRestAPI(Resource):
    def post(self):
        comp_json = request.get_json()
        repo = ComplaintRepository(db_session)
        compd = Complaint(**comp_json)
        res = repo.insert(compd)
        if res:
            content = jsonify(comp_json)
            return make_response(content,201)
        else:
            content = jsonify(message='Error in Complaint insert')
            return make_response(content,500)

class UpdateComplainantRestAPI(Resource):
    def patch(self,id):
        comp_json = request.get_json()
        repo = ComplaintRepository(db_session) 
        res = repo.update(id,comp_json)
        if res:
            content = jsonify(comp_json)
            return make_response(content,201)
        else:
            content = jsonify(message='Error Complaint Patch')
            return make_response(content,500)

class DeleteComplaintRestAPI(Resource):
    def delete(self,id):
        repo = ComplaintRepository(db_session)
        res = repo.delete(id)
        if res:
            content = jsonify(message = f'Complaint {id} delete')
            return make_response(content,201)
        else:
            content = jsonify(message='Error in Complaint delete') 
            return make_response(content,500)

class UpdateComplaintRestAPI(Resource):
    def put(self):
        comp_json = request.get_json()
        repo = ComplaintRepository(db_session)
        res = repo.update(comp_json['id'],comp_json)
        if res:
            content = jsonify(comp_json)
            return make_response(content,201)
        else:
            content = jsonify(message='Error in Complaint Put')
            return make_response(content,500)