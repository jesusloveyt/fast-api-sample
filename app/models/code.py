from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


class CodeModel(Base):
    __tablename__ = "tb_code"
    codeId = Column("code_id", Integer(), primary_key=True, autoincrement=True)
    code = Column("code", String(30))
    parentCode = Column("p_code", String(30))
    codeLabel = Column("code_label", String(60))
    memo = Column("memo", String(120))
    stringValue = Column("str_val", String(256))
    numberValue = Column("num_val", Float())
    useFlag = Column("use_fg", Boolean)
    editedAt = Column("edited_at", DateTime(), default=current_timestamp())
