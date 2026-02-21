import re
from datetime import datetime, timedelta, timezone

def parse_datetime_with_tz(s):
    match = re.match(r'^(\d{4}-\d{2}-\d{2}) UTC([+-])(\d{2}):(\d{2})$', s)
    date_str = match.group(1)
    sign = match.group(2)
    hours = int(match.group(3))
    minutes = int(match.group(4))
    
    offset = timedelta(hours=hours, minutes=minutes)
    if sign == '-':
        offset = -offset
    
    dt = datetime.fromisoformat(date_str)
    dt = dt.replace(tzinfo=timezone(offset))
    return dt

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_birthday_date(birth, target_year):
    month = birth.month
    day = birth.day
    
    if month == 2 and day == 29 and not is_leap_year(target_year):
        day = 28
    
    return datetime(target_year, month, day, tzinfo=birth.tzinfo)

birth = parse_datetime_with_tz(input().strip())
current = parse_datetime_with_tz(input().strip())

birth_utc = birth.astimezone(timezone.utc)
current_utc = current.astimezone(timezone.utc)

this_year_birth = get_birthday_date(birth, current_utc.year)
this_year_birth_utc = this_year_birth.astimezone(timezone.utc)

if this_year_birth_utc >= current_utc:
    diff = this_year_birth_utc - current_utc
else:
    next_year_birth = get_birthday_date(birth, current_utc.year + 1)
    next_year_birth_utc = next_year_birth.astimezone(timezone.utc)
    diff = next_year_birth_utc - current_utc

days = diff.total_seconds() / 86400

if abs(diff.total_seconds()) < 1:
    print(0)
else:
    print(int(days))