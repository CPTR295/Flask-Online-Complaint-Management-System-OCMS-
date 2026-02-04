from flask import make_response,jsonify,request
from flask_restful import Resource

from main_cache import cache
from model.config import db_session
from model.db import ComplaintDetails
from modules.complaint.repository.complaint_details import ComplaintDetailsRepository

class ListComplaintDetailsRestAPI(Resource):
    @cache.cached(timeout=50)
    def get(self):
        repo = ComplaintDetailsRepository(db_session)
        recs = repo.select_all()
        rec = [rec.to_json() for rec in recs]
        return make_response(jsonify(rec),200)

class AddComplaintDetailsRestAPI(Resource):
    def post(self):
        comp_details = request.get_json()
        repo = ComplaintDetailsRepository(db_session)
        compd = ComplaintDetails(**comp_details)
        res = repo.insert(compd)
        if res:
            content = jsonify(comp_details)
            return make_response(content,201)
        else:
            content = jsonify(message='Error in ComplaintDetails insert')
            return make_response(content,500)

class UpdateComplaintDetailsResolutionRestAPI(Resource):
    def patch(self,compid):
        comp_details = request.get_json()
        repo = ComplaintDetailsRepository(db_session) 
        res = repo.update(compid,comp_details)
        if res:
            content = jsonify(comp_details)
            return make_response(content,201)
        else:
            content = jsonify(message='Error ComplaintDetails Patch')
            return make_response(content,500)

class DeleteComplaintDetailsRestAPI(Resource):
    def delete(self,compid):
        repo = ComplaintDetailsRepository(db_session)
        res = repo.delete(compid)
        if res:
            content = jsonify(message = f'ComplaintDetails {compid} delete')
            return make_response(content,201)
        else:
            content = jsonify(message='Error in ComplaintDetails delete') 
            return make_response(content,500)

class UpdateComplaintDetailsRestAPI(Resource):
    def put(self):
        comp_details = request.get_json()
        repo = ComplaintDetailsRepository(db_session)
        res = repo.update(comp_details['compid'],comp_details)
        if res:
            content = jsonify(comp_details)
            return make_response(content,201)
        else:
            content = jsonify(message='Error in ComplaintDetails Put')
            return make_response(content,500)