# app/models.py

# SQLAlchemyのカラム、整数、文字列をインポート
from sqlalchemy import Column, Integer, String
# データベースのベースクラスをインポート
from app.database import Base

# ユーザークラスの定義
class User(Base):
    # テーブル名を指定
    __tablename__ = "users"

    # ユーザーIDのカラム定義
    id = Column(Integer, primary_key=True, index=True)
    # ユーザー名のカラム定義
    name = Column(String, index=True)
    # ユーザーのメールアドレスのカラム定義
    email = Column(String, unique=True, index=True)

    # デバッグ用のメッセージ
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

    # デバッグ用のメッセージ
    def __init__(self, name: str, email: str):
        print(f"\033[93m[DEBUG] : Initializing User with name={name}, email={email}\033[0m")
        self.name = name
        self.email = email

    # エラーハンドリングのためのメソッド
    def save(self, session):
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"\033[93m[DEBUG] : Error saving User(name={self.name}, email={self.email}): {e}\033[0m")
            raise e
