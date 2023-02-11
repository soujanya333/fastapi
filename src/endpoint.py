
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from src.schema import UserLog
from src.databse import Base, engine, SessionLocal, UserInfo
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException,  status, Security
import datetime



Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

api = APIRouter()


@api.post("/add/user_info/")
async def adduser(user: UserLog, db: Session = Depends(get_database_session)):
    user_info = {"firstname":user.firstname ,"lastname":user.lastname,"email":user.email,"mobile_no":user.mobile_no}

    data = UserInfo(firstname = user_info.get('firstname'),
                    lastname = user_info.get('lastname'),
                    email = user_info.get('email'),
                    mobile_no = user_info.get('mobile_no'),
                    )

    db.add(data)
    db.commit()
    return JSONResponse(content={"msg":"user added successfully", 'status': 200})





@api.get("/getalluser")
async def getall(db: Session = Depends(get_database_session)):
    try:
        result = db.query(UserInfo).all()
        response = []
        for i in result:
            result_dict  = {}
            result_dict['id'] = i.id
            result_dict['firstname'] = i.firstname
            result_dict['lastname'] = i.lastname
            result_dict['email'] = i.email
            result_dict['conatct'] = i.mobile_no
            response.append(result_dict)
        return response

    except Exception as e:
        return JSONResponse(content={"msg":e, 'status':404})






@api.put("/update/{id}/")
async def edituser(id : int ,user: UserLog, db: Session = Depends(get_database_session)):
    try:
        existing_item = db.query(UserInfo).filter(UserInfo.id == id).first()
        existing_item.firstname= user.firstname
        existing_item.lastname= user.lastname
        existing_item.email = user.email
        existing_item.mobile_no = str(user.mobile_no)
        db.add(existing_item)
        db.commit()
        return JSONResponse(content={"msg":"user edited successfully", 'status': 204})
        
    except:
        return HTTPException(status_code=404, detail="User not found")




@api.delete("/delete/{id}/")
async def delete(id:int, db: Session = Depends(get_database_session)):
    try:
        data = db.query(UserInfo).filter(UserInfo.id == id).first()
        db.delete(data)
        db.commit()
        return JSONResponse(content={"msg":"user deleted successfully",'status': 202})
    except:
        return HTTPException(status_code=404, detail="User not found")

