# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models, schemas
import dotenv
import os

# .envファイルから環境変数をロード
dotenv.load_dotenv()

# 環境変数DATABASE_URLを取得
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"\033[93m[DEBUG] : DATABASE_URL = {DATABASE_URL}\033[0m")

# FastAPIのインスタンスを作成
app = FastAPI()

# DBモデルをテーブルとして作成
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print(f"[DEBUG] : Error in create_user - {e}")
        raise HTTPException(status_code=400, detail=f"User could not be created: {e}")
