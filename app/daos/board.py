from sqlalchemy import Update
from sqlalchemy.sql.functions import current_timestamp

from common.db.query_worker import query_data
from common.db.context import session_maker
from models.board import BoardModel


def query_list(
    useFlag: bool = True,
    schTxt: str = None,
    boardKind: str = None,
    listCount: int = None,
    skipCount: int = None,
) -> list[BoardModel]:
    where_sql = "WHERE 1 = 1"
    params = {}
    if useFlag:
        where_sql += " AND bod.use_fg = %(useFlag)s"
        params["useFlag"] = useFlag
    if boardKind:
        where_sql += " AND bod.board_kind = %(boardKind)s"
        params["boardKind"] = boardKind
    if schTxt:
        where_sql += """ AND (
            ( bod.title     LIKE concat('%%', %(schTxt)s, '%%') ) OR
            ( bod.contents  LIKE concat('%%', %(schTxt)s, '%%') ) OR
            ( usr.user_name LIKE concat('%%', %(schTxt)s, '%%') )
            )"""
        params["schTxt"] = schTxt

    list_sql = f"""
        SELECT bod.*
            ,usr.user_name
            ,IFNULL(cod.code_label, bod.board_kind) AS boardKindName
            ,fle.file_url
        FROM tb_board bod
        JOIN tb_account usr ON usr.account_id = bod.writer_id
        LEFT JOIN tb_code cod ON cod.p_code = 'BOARD_KIND' and cod.code = bod.board_kind
        LEFT JOIN tb_file fle ON fle.link_info = 'boardMainImage' and fle.link_key = bod.board_id AND fle.deleted_at is NULL
        {where_sql}
        ORDER BY bod.board_id DESC
    """
    if listCount:
        list_sql += f" LIMIT {skipCount or 0}, {listCount}"

    rows = query_data(list_sql, params)
    if not rows or len(rows) == 0:
        return []

    board_list: list[BoardModel] = []
    for row in rows:
        board = BoardModel()
        board.boardId = row["board_id"]
        board.boardKind = row["board_kind"]
        board.boardKindName = row["boardKindName"]
        board.writerId = row["writer_id"]
        board.writerName = row["user_name"]
        board.title = row["title"]
        board.contents = row["contents"]
        board.readCount = row["read_count"]
        board.updatedAt = row["updated_at"]
        if "file_url" in row:
            board.mainImage.fileUrl = row["file_url"]

        board_list.append(board)

    return board_list


def get_list(
    useFlag: bool = True,
    schTxt: str = None,
    boardKind: str = None,
    listCount: int = None,
    skipCount: int = None,
) -> list[BoardModel]:
    with session_maker() as session:
        board_list_query = session.query(BoardModel).filter(
            BoardModel.useFlag == useFlag
        )
        if boardKind:
            board_list_query = board_list_query.filter(
                BoardModel.boardKind == boardKind
            )
        if schTxt:
            board_list_query = board_list_query.filter(
                BoardModel.title.like(f"%{schTxt}%")
                | BoardModel.contents.like(f"%{schTxt}%")
            )
        if skipCount:
            board_list_query = board_list_query.offset(skipCount)
        if listCount:
            board_list_query = board_list_query.limit(listCount)

        board_list = board_list_query.all()
        return board_list


def get_by_id(boardId: int) -> BoardModel:
    with session_maker() as session:
        board = session.query(BoardModel).filter(BoardModel.boardId == boardId).first()
        return board


def insert(boardKind: str, title: str, writerId: int, contents: str) -> BoardModel:
    with session_maker.begin() as session:
        new_board = BoardModel()
        new_board.boardKind = boardKind
        new_board.writerId = writerId
        new_board.title = title
        new_board.contents = contents
        new_board.readCount = 0
        new_board.useFlag = True
        new_board.createdAt = current_timestamp()
        new_board.updatedAt = current_timestamp()

        session.add(new_board)
        session.flush()
        session.refresh(new_board)
        return new_board


def update(
    boardId: int,
    boardKind: str = None,
    title: str = None,
    writerId: int = None,
    contents: str = None,
) -> bool:
    with session_maker.begin() as session:
        update_values = {BoardModel.updatedAt: current_timestamp()}

        if boardKind:
            update_values[BoardModel.boardKind] = boardKind

        if title:
            update_values[BoardModel.title] = title

        if writerId:
            update_values[BoardModel.writerId] = writerId

        if contents:
            update_values[BoardModel.contents] = contents

        session.execute(
            Update(BoardModel)
            .where(BoardModel.boardId == boardId)
            .values(update_values)
        )
        return True


def delete_using_flag(boardId: int) -> bool:
    with session_maker.begin() as session:
        session.execute(
            Update(BoardModel)
            .where(BoardModel.boardId == boardId)
            .values({BoardModel.useFlag: False})
        )
        return True
