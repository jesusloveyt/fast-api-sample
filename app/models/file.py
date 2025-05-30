from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


class FileModel(Base):
    __tablename__ = "tb_file"
    fileId = Column("file_id", Integer(), primary_key=True, autoincrement=True)
    linkInfo = Column("link_info", String(30))
    linkKey = Column("link_key", Integer())
    realName = Column("real_name", String(120))
    fileUrl = Column("file_url", String(120))
    fileSize = Column("file_size", Integer())
    savedAt = Column("saved_at", DateTime(), default=current_timestamp())
    deletedAt = Column("deleted_at", DateTime())

    def __init__(self):
        self.base64String = ""
