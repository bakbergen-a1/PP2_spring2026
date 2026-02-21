import re
from datetime import datetime, timedelta, timezone

def parse_datetime_with_tz(s):
    
    match = re.match(r'^(\d{4}-\d{2}-\d{2}) UTC([+-])(\d{2}):(\d{2})$', s)
    if not match:
        raise ValueError(f"Invalid format: {s}")
    
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

dt1 = parse_datetime_with_tz(input().strip())
dt2 = parse_datetime_with_tz(input().strip())

diff = abs(dt1 - dt2)

days = diff.days

print(days)