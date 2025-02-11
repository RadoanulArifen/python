def multiplication_table(n, limit=10):
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)

def subtract(a, b):
    return a - b

a=10
b=5
print(subtract(a, b))


def add_ten(n):
    m=n+10
    return m
another=add_ten(10)
print(another)