def read_side():
    return float(input("Введіть довжину сторони: "))

def is_square(a, b, c, d):
    return a == b == c == d

def is_rectangle(a, b, c, d):
    return a**2 + b**2 == c**2 + d**2

def square_area(a):
    return a**2

def rectangle_area(a, b):
    return a * b

a = read_side()
b = read_side()
c = read_side()
d = read_side()

if is_square(a, b, c, d):
    print("Це квадрат")
    print("Площа:", square_area(a))
elif is_rectangle(a, b, c, d):
    print("Це прямокутник")
    print("Площа:", rectangle_area(a, b))
else:
    print("Це не квадрат і не прямокутник")

#2
print("EX 2")

import random

def create_email(domains, names):
    surname = random.choice(names)
    number = random.randint(100, 999)
    letters = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randint(5, 7)))
    domain = random.choice(domains)
    email = f"{surname}.{number}@{letters}.{domain}"
    return email

names = ["smit", "miller", "melnyk"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)


