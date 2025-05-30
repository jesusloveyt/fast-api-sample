from typing import Optional

from fastapi import Query
from pydantic import BaseModel

from dtos.base import BaseParam, BaseResult
from dtos.file import FileSchema


class BoardSchema(BaseModel):
    boardId: Optional[int] = 0
    boardKind: Optional[str] = None
    writerId: Optional[int] = 0
    title: Optional[str] = None
    contents: Optional[str] = None


class BoardResult(BoardSchema, BaseResult):
    readCount: Optional[int] = 0
    writerName: Optional[str] = None
    boardKindName: Optional[str] = None
    mainImage: Optional[FileSchema] = None

    class Config:
        from_attributes = True


class BoardParam(BaseParam):
    boardKind: str = Query(None)


class BoardForm(BoardSchema):
    mainImage: Optional[FileSchema] = None
