# 1
first_list = [1, 'one', 5, 'y', 3, 0, 2, 8, 'a']
second_list =  [0, 1, 2, 3, 4, 5, 0, 'a', 0, 1, 2, 3]
first_set = set(first_list)
second_set = set(second_list)
print(first_set.intersection(second_set))
print() # Використовую суто для відступів при виводі

#2
print("Ex 2")
students = {'Sydorenko': 101, 'Vasylenko': 102, 'Pavlenko': 99, 'Smyrnov': 100}
sum = 0
for k in students:
    sum += students[k]
avarage_mark = sum/len(students)
print(avarage_mark)

for name in students.keys():
    if students[name] > avarage_mark:
        print(name)
print()

#3
print("Ex 3")
list_test = [1, 2, 3, 4, 5, 6, 1, 1, 8, 8, 9, 5, 4, 7, 6, 10, 7]

unique_numbers = set(list_test)
count = len(unique_numbers)

print("Кількість різних значень:", count, '\n')

#4
print("Ex 4")
list1 = list(input("Enter your first list: ").split())
list2 = list(input("Enter your srcond list: ").split())

common_numbers = set(list1).intersection(set(list2))

for num in sorted(common_numbers):
    print(num, end=' ')
print()

#5
print("Ex 5")
text = input("Enter your text please: ")
words = text.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word, freq in word_freq.items():
    print(word, freq)



