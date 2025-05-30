from models.file import FileModel
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


class AccountModel(Base):
    __tablename__ = "tb_account"
    accountId = Column("account_id", Integer(), primary_key=True, autoincrement=True)
    joinType = Column("join_type", String(10))
    accountKey = Column("account_key", String(30))
    password = Column("password", String(256))
    snsKey = Column("sns_key", String(60))
    companyId = Column("company_id", Integer())
    userName = Column("user_name", String(30))
    phone = Column("phone", String(15))
    email = Column("email", String(100))
    address = Column("address", String(120))
    role = Column("role", String(20))
    level = Column("level", String(20))
    fcmToken = Column("fcm_token", String(256))
    refreshToken = Column("refresh_token", String(140))
    useFlag = Column("use_fg", Boolean)
    createdAt = Column("created_at", DateTime(), default=current_timestamp())
    updatedAt = Column("updated_at", DateTime(), default=current_timestamp())
    loginAt = Column("login_at", DateTime())
    passwordAt = Column("password_at", DateTime())

    def __init__(self):
        self.companyName = ""
        self.profileImage = FileModel()
