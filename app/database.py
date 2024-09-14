# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 環境変数をロードする
load_dotenv()

# データベースURLを環境変数から取得する
DATABASE_URL = os.getenv("DATABASE_URL")

# デバッグメッセージ
print(f"\033[93m[DEBUG] : DATABASE_URL = {DATABASE_URL}\033[0m")

# データベースエンジンを作成する
engine = create_engine(DATABASE_URL)
# デバッグメッセージ
print(f"\033[93m[DEBUG] : Engine created with DATABASE_URL\033[0m")

# セッションローカルを作成する
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# デバッグメッセージ
print(f"\033[93m[DEBUG] : SessionLocal created\033[0m")

# ベースクラスを作成する
Base = declarative_base()
# デバッグメッセージ
print(f"\033[93m[DEBUG] : Base declarative class created\033[0m")

# DB接続用のセッションを取得する関数
def get_db():
    # デバッグメッセージ
    print(f"\033[93m[DEBUG] : Entering get_db function\033[0m")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        # デバッグメッセージ
        print(f"\033[93m[DEBUG] : Database session closed\033[0m")
