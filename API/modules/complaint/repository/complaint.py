from typing import Dict,Any,List
from model.db import Complaint
from sqlalchemy.orm import Session
from main_cache import cache

class ComplaintRepository:
    def __init__(self,sess:Session):
        self.sess = sess

    def insert(self,com:Complaint)->bool:
        try:
            self.sess.add(com)
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return False

    def update(self,id:int,details:Dict[str,Any])->bool:
        try:
            self.sess.query(Complaint).filter(Complaint.id==id).update(details)
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return False
    
    def delete(self,id:int)->bool:
        try:
            self.sess.query(Complaint).filter(Complaint.id==id).delete()
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return False
    
    @cache.memoize(timeout=50)
    def select_all(self)->List[Any]:
        coms = self.sess.query(Complaint).all()
        return coms
    
    def select_one(self,id:int)->Any:
        com = self.sess.query(Complaint).filter(Complaint.id==id).one_or_none()
        return com