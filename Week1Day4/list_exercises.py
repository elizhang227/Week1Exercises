# title = "Green Lantern Corp"
# counter = 0
# while counter < len(title):
#     print(title[counter])
#     counter += 1

# Sum the Numbers
"""
numbers = [3, 2, 5, 22, 55]
total = 0
for number in numbers:
    total = total + number
print(total)
"""
# Largest Number
"""
numbers = [3, 2, 5, 22, 55]
for number in numbers:
    if number == max(numbers):
        print(max(numbers))
"""
# Smallest Number
"""
numbers = [3, 2, 5, 22, 55]
for number in numbers:
    if number == min(numbers):
        print(min(numbers))
"""
# Even Numbers
"""
numbers = [3, 2, 5, 22, 55]
for number in numbers:
    if number % 2 == 0:
        print(number)
"""
# Positive Numbers
"""
numbers = [3, 2, -5, 32, 55, -42]
for number in numbers:
    if number > 0:
        print(number)
"""
# Positive Numbers 2 with own numbers
"""
positive_list = []
numbers = [3, 2, -5, 32, 55, -42]
for number in numbers:
    if number > 0:
        positive_list.append(number)
print(positive_list)
"""
# With user inputed numbers
""""
numbers = [] # creates empty list for user inputs to go into
positive_list = [] # creates empty list for positive numbers to go into
x = 0
#asks user for 5 inputs
while x < 5:
    numbers.append(int(input('Please enter some numbers: ')))
    x += 1
#appends positive numbers to new list
for number in numbers:
    if number > 0:
        positive_list.append(number)
#prints both on the same line
print('The positive numbers from your list are: ', end="") 
print(positive_list)
"""

# Multiply a list
"""
numbers = [2, 3, 5, 6, 7, 39, 45]
multiplied = []
factor = 4

for number in numbers:
    multiplied.append(number * factor)
print(multiplied)
"""

# Multiply Vectors
"""
list1 = [2, 4, 5, 6]
list2 = [3, 22, 7, 9]
newlist = []

#for number in list1:
newlist.append(list1[0] * list2[0])
newlist.append(list1[1] * list2[1])
newlist.append(list1[2] * list2[2])
newlist.append(list1[3] * list2[3])
print(newlist)
"""

# Matrix Addition
"""
X = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
"""

# Matrix Addition 2
for i in range(len(X)): #iterate through rows    
        if 
# De-dup
"""
list = [2, 4, 5, 4, 2, 5, 3, 8, 7]
newlist = []
seen = set()

for number in list:
    if number not in seen:
        newlist.append(number)
        seen.add(number)
print(newlist)
"""

