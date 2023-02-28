# Exersice 1

print('Exersice 1', '\n')

import random

min = random.randint(0, 59)
print(min)
if min <= 15:
    print("Your number belongs to the first quarter")
elif 15 < min <= 30:
    print("Your number belongs to the second quarter")
elif 30 < min <= 45:
    print("Your number belongs to the third quarter")
elif 45 < min <= 59:
    print("Your number belongs to the fourth quarter")

# Exersice 2

print('\n' , 'Exersice 2', '\n')

birth_month = int(input("Please enter month of your birth: "))

if 0 < birth_month <= 2 or birth_month == 12:
    print("Зима - За вікном падав сніг")
elif 2 < birth_month <= 5:
    print("Весна - Все довкола розцвітало.")
elif 5 < birth_month <= 8:
    print("Літо - Діти насолоджувались літніми канікулами.")
elif 8 < birth_month <= 11:
    print("Осінь - Все довкола загоралось яскравими фарбами.")
else:
    print("You have entered an incorrect birth month, please try again")


# Exersice 3

print('\n' , 'Exersice 3', '\n')

your_number = random.randint(0, 1000000)
print(your_number)
total_sum = 0
while your_number > 0:
    digit = your_number % 10
    total_sum = total_sum + digit
    your_number = your_number // 10
print(total_sum)

print((your_number % 2 == 0) and (total_sum % 3 == 0)) #Інколи видає TRUE, коли число не ділиться без остачі на 2, чому так відпрацьовує?
print(your_number % 2) #Інколи повертає 0, коли частка не 0
print(your_number // 2) #Інколи повертає 0, коли частка не 0

if ((your_number % 2 == 0) and (total_sum % 3 == 0)):
    print("Your number is divisible by 6")
else:
    print("Your number is NOT divisible by 6")

# Exersice 4

print('\n' , 'Exersice 4', '\n')

x = int(input("Enter x: "))
y = int(input("Enter y: "))
if (x > 0 and y > 0):
    print("Your point belongs to the first quarter")
elif (x < 0 and y > 0):
    print("Your point belongs to the second quarter")
elif (x < 0 and y < 0):
    print("Your point belongs to the third quarter")
elif (x > 0 and y < 0):
    print("Your point belongs to the fourth quarter")
elif (x == 0 or y == 0):
    print("Your point is on the coordinate line")