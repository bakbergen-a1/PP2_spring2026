import re
from datetime import datetime, timedelta, timezone

def parse_datetime_with_tz(s):
    match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC([+-])(\d{2}):(\d{2})$', s)
    if not match:
        raise ValueError(f"Invalid format: {s}")
    
    datetime_str = match.group(1)
    sign = match.group(2)
    hours = int(match.group(3))
    minutes = int(match.group(4))
    
    offset = timedelta(hours=hours, minutes=minutes)
    if sign == '-':
        offset = -offset
    
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    
    dt = dt.replace(tzinfo=timezone(offset))
    
    return dt

start = parse_datetime_with_tz(input().strip())
end = parse_datetime_with_tz(input().strip())

start_utc = start.astimezone(timezone.utc)
end_utc = end.astimezone(timezone.utc)

duration = int((end_utc - start_utc).total_seconds())

print(duration)