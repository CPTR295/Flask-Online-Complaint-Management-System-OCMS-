from flask import make_response,jsonify,request
from flask_restful import Resource

from main_cache import cache
from model.config import db_session
from model.db import ComplaintType
from modules.complaint.repository.complaint_type import ComplaintTypeRepository

class ListComplaintTypeRestAPI(Resource):
    @cache.cached(timeout=50)
    def get(self):
        repo = ComplaintTypeRepository(db_session)
        recs = repo.select_all()
        rec = [rec.to_json() for rec in recs]
        return make_response(jsonify(rec),200)

class AddComplaintTypeRestAPI(Resource):
    def post(self):
        comptype_json = request.get_json()
        repo = ComplaintTypeRepository(db_session)
        compd = ComplaintType(**comptype_json)
        res = repo.insert(compd)
        if res:
            content = jsonify(comptype_json)
            return make_response(content,201)
        else:
            content = jsonify(message='Error in ComplaintType insert')
            return make_response(content,500)

class UpdateComplaintTypeNameRestAPI(Resource):
    def patch(self,id):
        comptype_json = request.get_json()
        repo = ComplaintTypeRepository(db_session) 
        res = repo.update(id,comptype_json)
        if res:
            content = jsonify(comptype_json)
            return make_response(content,201)
        else:
            content = jsonify(message='Error ComplaintType Patch')
            return make_response(content,500)

class DeleteComplaintTypeRestAPI(Resource):
    def delete(self,id):
        repo = ComplaintTypeRepository(db_session)
        res = repo.delete(id)
        if res:
            content = jsonify(message = f'ComplaintType {id} delete')
            return make_response(content,201)
        else:
            content = jsonify(message='Error in ComplaintType delete') 
            return make_response(content,500)

class UpdateComplaintTypeRestAPI(Resource):
    def put(self):
        comptype_json = request.get_json()
        repo = ComplaintTypeRepository(db_session)
        res = repo.update(comptype_json['id'],comptype_json)
        if res:
            content = jsonify(comptype_json)
            return make_response(content,201)
        else:
            content = jsonify(message='Error in ComplaintType Put')
            return make_response(content,500)