# Reading file content

with open("sample.txt", "r") as f:
    print("Using read():")
    print(f.read())

with open("sample.txt", "r") as f:
    print("\nUsing readline():")
    print(f.readline())

with open("sample.txt", "r") as f:
    print("\nUsing readlines():")
    print(f.readlines())