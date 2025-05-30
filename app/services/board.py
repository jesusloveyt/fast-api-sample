from daos import board as board_dao
from daos import file as file_dao

from models.board import BoardModel
from dtos.board import BoardForm, BoardResult


def get_board_list(
    useFlag: bool = True,
    schTxt: str = None,
    boardKind: str = None,
    listCount: int = None,
    skipCount: int = None,
) -> list[BoardResult]:
    return board_dao.query_list(
        useFlag=useFlag,
        schTxt=schTxt,
        boardKind=boardKind,
        listCount=listCount,
        skipCount=skipCount,
    )


def get_board_by_id(boardId: int) -> BoardModel:
    board = board_dao.get_by_id(boardId)
    if not board:
        return None
    board_data = BoardResult.model_validate(board)
    board_data.mainImage = file_dao.get_by_link("boardMainImage", boardId)
    return board_data


def add_board(boardForm: BoardForm) -> BoardModel:
    board = board_dao.insert(
        boardForm.boardKind, boardForm.title, boardForm.writerId, boardForm.contents
    )
    if not board:
        return None
    if boardForm.mainImage:
        file_dao.insert(
            "boardMainImage",
            board.boardId,
            boardForm.mainImage.realName,
            boardForm.mainImage.fileUrl,
            boardForm.mainImage.fileSize,
        )
    return board


def update_board(boardForm: BoardForm) -> bool:
    board_dao.update(
        boardForm.boardId,
        boardForm.boardKind,
        boardForm.title,
        boardForm.writerId,
        boardForm.contents,
    )
    mainImage = boardForm.mainImage
    if mainImage:
        fileId = mainImage.fileId
        if not fileId or fileId == 0:
            file_dao.delete_using_flag(
                linkInfo="boardMainImage", linkKey=boardForm.boardId
            )

        if mainImage.realName and mainImage.fileUrl:
            file_dao.insert(
                "boardMainImage",
                boardForm.boardId,
                mainImage.realName,
                mainImage.fileUrl,
                mainImage.fileSize,
            )
    else:
        file_dao.delete_using_flag(linkInfo="boardMainImage", linkKey=boardForm.boardId)

    return True


def delete_board(boardId: int) -> bool:
    return board_dao.delete_using_flag(boardId)
