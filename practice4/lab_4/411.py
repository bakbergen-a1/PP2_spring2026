import json
import sys

def apply_patch(source, patch):
    if patch is None:
        return None
    if isinstance(source, dict) and isinstance(patch, dict):
        result = source.copy()
        for key, value in patch.items():
            if value is None:
                result.pop(key, None)
            elif key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = apply_patch(result[key], value)
            else:
                result[key] = value
        return result
    else:
        return patch

source = json.loads(sys.stdin.readline().strip())
patch = json.loads(sys.stdin.readline().strip())

result = apply_patch(source, patch)

print(json.dumps(result, separators=(',', ':'), sort_keys=True))