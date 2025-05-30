from datetime import datetime


def get_datetime_text_from_timestamp(dt_val: datetime):
    return f"{dt_val.year}년 {dt_val.month}월 {dt_val.day}일 {dt_val.hour}시 {dt_val.minute}분"


def get_datetime_text_from_str(str_val: str):
    month = int(str_val[5:7])
    day = int(str_val[8:10])
    hour = int(str_val[11:13])
    minute = int(str_val[14:16])
    return f"{str_val[:4]}년 {month}월 {day}일 {hour}시 {minute}분"
