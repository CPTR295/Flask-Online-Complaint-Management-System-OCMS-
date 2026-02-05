from typing import List,Any,Dict
from model.db import Administrator
from sqlalchemy.orm import Session 

class AdminRepository:
    def __init__(self,sess:Session):
        self.sess = sess

    def insert(self,Admin:Administrator)->bool:
        try:
            self.sess.add(Admin)
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return False
    
    def update(self,id:int,details:Dict[str,Any])->bool:
        try:
            self.sess.query(Administrator).filter(Administrator.id==id).update(details)
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return   False
    
    def delete(self,id:int)->bool:
        try:
            self.sess.query(Administrator).filter(Administrator.id==id).delete()
            self.sess.commit()
            return True
        except Exception as e:
            print(e)
        return False
    
    def select_all(self)->List[Any]:
        recs = self.sess.query(Administrator).all()
        return recs 

    def select_one(self,id:int)->Any:
        rec = self.sess.query(Administrator).filter(Administrator.id==id).one_or_none()
        return rec