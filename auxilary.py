from datetime import datetime


def remove_brackets(text: str):
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


def validate_dates(start_date: str, final_date: str):
    """Check for dates' validity"""
    start = datetime.strptime(start_date, '%d.%m.%Y')
    final = datetime.strptime(final_date, '%d.%m.%Y')
    if final < start:
        raise ValueError("Final date shouldn't be earlier than the start date")
