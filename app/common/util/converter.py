from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.ext.declarative import DeclarativeMeta

T = TypeVar("T", bound=BaseModel)
M = TypeVar("M", bound=DeclarativeMeta)


def dto_to_model(dto: T, model_class: Type[M]) -> M:
    model = model_class()

    for field_name, field_value in dto.dict().items():
        # 모델에 해당 필드가 있는 경우에만 설정
        if hasattr(model, field_name):
            setattr(model, field_name, field_value)

    return model
