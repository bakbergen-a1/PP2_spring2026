import json
import sys
import re

def resolve_query(data, query):
    """Запрос бойынша JSON-дан мәнді табу"""
    current = data
    
    
    parts = query.split('.')
    
    for part in parts:
        
        match = re.match(r'^(.+?)(?:\[(\d+)\])?$', part)
        if not match:
            return None
        
        key = match.group(1)
        index = match.group(2)
        
        if key:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        
        if index is not None:
            idx = int(index)
            if isinstance(current, list) and 0 <= idx < len(current):
                current = current[idx]
            else:
                return None
    
    return current

data = json.loads(sys.stdin.readline().strip())

n = int(sys.stdin.readline().strip())

for _ in range(n):
    query = sys.stdin.readline().strip()
    result = resolve_query(data, query)
    
    if result is None:
        print("NOT_FOUND")
    else:
        print(json.dumps(result, separators=(',', ':')))