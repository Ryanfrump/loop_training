def add(x:float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square(x: float) -> float:
    return x * x

def add_square(x: float, y: float) -> float:
    return x * x + y * y
a = add(3,4)
b = multiply(4,6)
c = square(2)
d = add_square(2,3)
print(a)
print(b)
print(c)
print(d)