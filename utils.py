from datetime import datetime
from dateutil.relativedelta import relativedelta


def remove_brackets(text: str) -> str:
    """Remove brackets and text inside"""
    if any(bracket in ('(', ')') for bracket in text):
        ret = ''
        skip1c = 0
        skip2c = 0
        for char in text:
            if char == '(':
                skip2c += 1
            elif char == ')' and skip2c > 0:
                skip2c -= 1
            elif skip1c == 0 and skip2c == 0:
                ret += char
        return ret.strip()
    return text.strip()


def validate_dates(start_date: str, final_date: str) -> bool:
    """Check for dates' validity"""
    start = datetime.strptime(start_date, '%d.%m.%Y')
    final = datetime.strptime(final_date, '%d.%m.%Y')
    return True if final < start else False


def create_period(start_month: int, start_year: int) -> str:
    """Creates a period of dates. Each string is a month that consists of the
    first and last dates of the month. Goes over new year only once."""
    last_date_of_month = datetime(start_year, start_month, 1) + relativedelta(
        months=1, days=-1)
    return f"{datetime(start_year, start_month, 1).strftime('%d.%m.%Y')}-" \
           f"{last_date_of_month.strftime('%d.%m.%Y')}"
