import sys
import importlib

def classify_attribute(module_path, attr_name):
    try:
        module = importlib.import_module(module_path)
    except (ImportError, ModuleNotFoundError):
        return "MODULE_NOT_FOUND"
    
    if not hasattr(module, attr_name):
        return "ATTRIBUTE_NOT_FOUND"
    
    attr = getattr(module, attr_name)
    
    if callable(attr):
        return "CALLABLE"
    else:
        return "VALUE"

n = int(sys.stdin.readline().strip())

for _ in range(n):
    line = sys.stdin.readline().strip().split()
    if len(line) == 2:
        module_path, attr_name = line
    else:
        continue
    
    result = classify_attribute(module_path, attr_name)
    print(result)