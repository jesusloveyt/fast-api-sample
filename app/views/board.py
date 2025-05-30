from typing import Optional
from fastapi import APIRouter
from fastapi import Query
from fastapi import Path

from common.api_result import ApiResult, ResultStatus
from models.board import BoardModel
from services import board as board_service
from dtos.board import BoardResult, BoardForm


router = APIRouter(prefix="/api/board")


@router.get("", response_model=ApiResult[list[BoardResult]])
async def get_board_list(
    useFlag: Optional[bool] = Query(True),
    schTxt: Optional[str] = Query(None),
    boardKind: Optional[str] = Query(None),
    listCount: Optional[int] = Query(0, ge=0),
    skipCount: Optional[int] = Query(0, ge=0),
) -> ApiResult[list[BoardResult]]:
    try:
        api_result = ApiResult[list[BoardResult]]()
        api_result.data = board_service.get_board_list(
            useFlag=useFlag,
            schTxt=schTxt,
            boardKind=boardKind,
            listCount=listCount,
            skipCount=skipCount,
        )
    except Exception as e:
        print("get_board_list Exception", e)
        api_result.status = ResultStatus.ERROR
        api_result.reason = "Exception"
        api_result.message = str(e)
    return api_result


@router.get("/{boardId}", response_model=ApiResult[BoardResult])
async def get_board_by_id(boardId: int = Path(..., ge=1)) -> ApiResult[BoardResult]:
    try:
        api_result = ApiResult[BoardResult]()
        board_data = board_service.get_board_by_id(boardId)
        if board_data:
            api_result.data = board_data
        else:
            api_result.status = ResultStatus.FAIL
            api_result.reason = "BoardNotFound"
    except Exception as e:
        print("get_board_by_id Exception", e)
        api_result.status = ResultStatus.ERROR
        api_result.reason = "Exception"
        api_result.message = str(e)
    return api_result


@router.post("", response_model=ApiResult[BoardResult])
async def add_board(boardForm: BoardForm) -> ApiResult[BoardModel]:
    try:
        api_result = ApiResult()
        board_data = board_service.add_board(boardForm)
        if board_data:
            api_result.data = board_data
        else:
            api_result.status = ResultStatus.FAIL
    except Exception as e:
        print("add_board Exception", e)
        api_result.status = ResultStatus.ERROR
        api_result.reason = "Exception"
        api_result.message = str(e)
    return api_result


@router.put("", response_model=ApiResult)
async def update_board(boardForm: BoardForm) -> ApiResult:
    try:
        api_result = ApiResult()
        result = board_service.update_board(boardForm)
        if not result:
            api_result.status = ResultStatus.FAIL
    except Exception as e:
        print("update_board Exception", e)
        api_result.status = ResultStatus.ERROR
        api_result.reason = "Exception"
        api_result.message = str(e)
    return api_result


@router.delete("/{boardId}", response_model=ApiResult)
async def delete_board(boardId: int = Path(..., ge=1)) -> ApiResult:
    try:
        api_result = ApiResult()
        result = board_service.delete_board(boardId)
        if not result:
            api_result.status = ResultStatus.FAIL
    except Exception as e:
        print("delete_board Exception", e)
        api_result.status = ResultStatus.ERROR
        api_result.reason = "Exception"
        api_result.message = str(e)
    return api_result
