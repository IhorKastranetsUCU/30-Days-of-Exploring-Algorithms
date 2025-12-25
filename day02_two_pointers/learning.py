def get_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def dislay_name(*args):
    for arg in args:
        print(arg, end=" ")

def print_adress(**kwargs):
    print(type(kwargs))
print_adress(street ="123 Fake", city="Detroid", state="MI", zip = "54321")