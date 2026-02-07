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

