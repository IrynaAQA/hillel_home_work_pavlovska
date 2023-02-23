# Exersice 1

print('Exersice 1', '\n')
first_name = str(input('Please, enter your first name: '))
last_name = str(input('Please, enter your last name: '))
personal_data = first_name + ' ' + last_name
print('You have registered as:', personal_data)

# 2

print('\n')
personal_data_low_case = str.lower(personal_data)
print('Your name in lower case: ', personal_data_low_case)
personal_data_cap_case = str.capitalize(personal_data)
print('Your name from capital letter: ', personal_data_cap_case)
personal_data_upper_case = str.upper(personal_data)
print('Your name in upper case: ', personal_data_upper_case)

# 3

print('\n')
personal_data_repeat = (personal_data + ' ') * 5
print(personal_data_repeat)

#4

print('\n')
personal_data = '\n' + '\t' + first_name + last_name + '\n'
print(personal_data)
personal_data = str.strip(personal_data)
print(personal_data)

# Exersice 2
import math

print('\n', 'Exersice 2', '\n')
radius = float(input('Enter radius of your circle: '))
square = math.pi * pow(radius, 2)
print('Square of your circle: ', round(square, 2))

# Exersice 3

print('\n', 'Exersice 3', '\n')
usd = 36.74
uah = float(input('Enter the amount in uah that you want to convert into dollars: '))
exchange_rate = uah / usd
exchange_rate = round(exchange_rate, 2)
print('The current rate is: ', exchange_rate)
