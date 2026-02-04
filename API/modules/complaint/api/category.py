from flask import jsonify , request ,make_response
from flask_restful import Resource

from main_cache import cache
from model.config import db_session
from model.db import Category
from modules.complaint.repository.category import CategoryRepository

class ListCategoryRestAPI(Resource):
    def get(self):
        repo = CategoryRepository(db_session)
        recs = repo.select_all()
        cat_rec = [rec.to_json() for rec in recs]
        return make_response(jsonify(cat_rec),201)

class AddCategoryRestAPI(Resource):
    @cache.cached(timeout=30)
    def post(self):
        cat_json = request.get_json()
        repo = CategoryRepository(db_session)
        category = Category(**cat_json)
        res = repo.insert(category)
        if res:
            content = jsonify(cat_json)
            return make_response(content,201)
        else:
            content = jsonify(message='Error in insert category')
            return make_response(content,500)
    
class UpdateCategoryNameRestAPI(Resource):
    def patch(self,id):
        cat_json = request.get_json()
        repo = CategoryRepository(db_session)
        res  = repo.update(id,cat_json)
        if res:
            content = jsonify(cat_json)
            return make_response(content,201)
        else:
            content = jsonify(message=f'Error in updaing category')
            return make_response(content,500)

class DeleteCategoryRestAPI(Resource):
    def delete(self,id):
        repo  = CategoryRepository(db_session)
        res = repo.delete(id)
        if res:
            content = jsonify(message=f'Delete Category with id: {id}')
            return make_response(content,201)
        else:
            content = jsonify(message='Error in category deletion')
            return make_response(content,500)

class UpdateCategoryRestAPI(Resource):
    def put(self):
        cat_json = request.get_json()
        repo = CategoryRepository(db_session)
        result = repo.update(cat_json['id'], cat_json)
        if result:
            content = jsonify(cat_json)
            return make_response(content, 201)
        else:
            content = jsonify(message="update complaint category record encountered a problem")
            return make_response(content, 500)