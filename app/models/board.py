from models.file import FileModel
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


class BoardModel(Base):
    __tablename__ = "tb_board"
    boardId = Column("board_id", Integer(), primary_key=True, autoincrement=True)
    boardKind = Column("board_kind", String(12))
    writerId = Column("writer_id", Integer())
    title = Column("title", String(90))
    contents = Column("contents", String(5000))
    readCount = Column("read_count", Integer())
    useFlag = Column("use_fg", Boolean)
    createdAt = Column("created_at", DateTime(), default=current_timestamp())
    updatedAt = Column("updated_at", DateTime(), default=current_timestamp())

    def __init__(self):
        self.mainImage = FileModel()
        self.writerName = ""
        self.boardKindName = ""
