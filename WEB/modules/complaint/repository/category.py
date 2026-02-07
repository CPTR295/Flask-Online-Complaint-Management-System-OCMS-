from typing import Dict, List, Any
from model.db import Category
from sqlalchemy.orm import Session 

class CategoryRepository:
    def __init__(self,sess:Session):
        self.sess = sess

    def insert(self,cat:Category)->bool:
        try:
            self.sess.add(cat)
            self.sess.commit()
            return True 
        except Exception as e:
            print(e)
        return False
    
    def update(self,id:int,details:Dict[str,Any])->bool:
        try:
            self.sess.query(Category).filter(Category.id==id).update(details)
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return False
    
    def delete(self,id:int)->bool:
        try:
            self.sess.query(Category).filter(Category.id==id).delete()
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return False
    
    def select_all(self)->List[Any]:
        cats = self.sess.query(Category).all() 
        return cats 
    
    def select_all(self,id:int):
        cat = self.sess.query(Category).filter(Category.id==id).one_or_none()
        return cat