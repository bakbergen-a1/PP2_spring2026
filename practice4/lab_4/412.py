import json
import sys

def find_diffs(a, b, path=""):
    diffs = []

    if type(a) != type(b):
        old = json.dumps(a, separators=(',', ':'))
        new = json.dumps(b, separators=(',', ':'))
        return [(path or "root", f"{old} -> {new}")]

    if isinstance(a, dict):
        all_keys = set(a) | set(b)
        for key in sorted(all_keys):
            new_path = f"{path}.{key}" if path else key
            
            if key not in a:
                val = json.dumps(b[key], separators=(',', ':'))
                diffs.append((new_path, f"<missing> -> {val}"))
            elif key not in b:
                val = json.dumps(a[key], separators=(',', ':'))
                diffs.append((new_path, f"{val} -> <missing>"))
            elif a[key] != b[key]:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    diffs.extend(find_diffs(a[key], b[key], new_path))
                else:
                    old = json.dumps(a[key], separators=(',', ':'))
                    new = json.dumps(b[key], separators=(',', ':'))
                    diffs.append((new_path, f"{old} -> {new}"))
    
    return diffs

a = json.loads(sys.stdin.readline())
b = json.loads(sys.stdin.readline())

diffs = find_diffs(a, b)

if diffs:
    for path, change in sorted(diffs):
        print(f"{path} : {change}")
else:
    print("No differences")