# Short hand if-else (ternary operator) examples

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

a, b = 10, 20
larger = a if a > b else b
print(larger)

num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)

score = 85
grade = "Pass" if score >= 60 else "Fail"
print(grade)

x = 15
message = "High" if x > 20 else "Medium" if x > 10 else "Low"
print(message)

value = 5
if value > 0: print("Positive")

age = 25
print("Adult") if age >= 18 else print("Minor")