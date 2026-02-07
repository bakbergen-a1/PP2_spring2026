def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)

def show_names(*names):
    for n in names:
        print(n)

show_names("Ali", "Dana")

def info(**data):
    print(data)

info(name="Aigerim", age=18)

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Aigerim", age = 18, city = "Almaty ")