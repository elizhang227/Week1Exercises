"""
bye_count = 0

while bye_count < 3:
    should_run = True

    while should_run:
        user_input = input("What? ")
        print("%s" % (user_input,))
        if user_input == "bye":
            should_run = False
            bye_count += 1
        print(bye_count)
"""

"""
i = 1

while i <= 10:
    print(i)
    i += 1
"""

"""
start = int(input('Start from: '))
end   = int(input('End on: '))

while start <= end:
    print(start)
    start += 1
"""

"""
i = 1

while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1
"""

"""
i = 0
print("You have %s coins. " % (i,))
choice = "yes"

while choice == "yes":
    choice = input("Do you want another? ")
    i += 1
    print("You have %s coins. " % (i,))
"""

"""
i = "* * * * *"
count = 0

while count <= 5:
    print(i)
    count += 1
"""

"""
i = "*"
count = 0
rows = int(input("How big is the square? "))

while count < rows:
    print(i * rows)
    count += 1
"""

"""
width = int(input("Width? "))
height = int(input("Height? "))
i = "*"
gap = " "
x = 1

while x <= height:
    if x == 1 or x == height:
        print(i * width)
    else:
        print(i + (gap * (width - 2))+ i)
    x += 1
"""

"""
# Print Triangle
i = "*"
gap = " "
x = 0
stars = 1
spaces = 3

while x < 4:
    if x == 0:
        print((gap * spaces) + i + (gap * spaces))
    else:
        print((gap * spaces) + (i * stars) + (gap * spaces))
    spaces -= 1
    x += 1
    stars += 2
"""

"""
# Print Triangle II
i = "*"
gap = " "
x = 0
asked_height = int(input("Enter a height: "))
stars = 1
spaces = (asked_height - 1)

while x < asked_height:
    if x == 0:
        print((gap * spaces) + i + (gap * spaces))
    else:
        print((gap * spaces) + (i * stars) + (gap * spaces))
    spaces -= 1
    x += 1
    stars += 2
"""

a = 1
b = 1


while True:
    if b <= 10:
        total = a * b
        print('%s x %s = %s' % (a, b, total))
        b += 1
    else:
        b = 1
        a += 1
    


# while True:
#     if a == 1 and b <= 10:
#         total = a * b
#         print('%s x %s = %s' % (a, b, total))
#     b += 1
#     elif a == 2 and b <= 10:
#         total = a * b
#         print('%s x %s = %s' % (a, b, total))  

"""
day = int(input('Day (0-6)? '))

while True:
    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    break
"""

"""
day = int(input('Day (0-6)? '))

while True:
    if day == 0 or day == 6:
        print("Sleep in")
    else:
        print("Go to work")
    break
"""

"""
temp = float(input("Temperature in C? "))

while True:
    farenheit = (temp * 1.8) + 32
    print(str(farenheit) + ' F')
    break
"""

"""
bill = float(input("Total bill amount: "))
service = input("Service? (good/fair/bad) ")

while True:
    if service == "good":
        tip = bill * .20
    elif service == "fair":
        tip = bill * .15
    elif service == "bad":
        tip = bill * .10
    break
print('Tip amount: %.2f' % tip)
print('Total amount: %.2f' % (tip + bill))
"""

"""
bill = float(input("Total bill amount: "))
service = input("Service? (good/fair/bad) ")
split = int(input("Split how many ways? "))

while True:
    if service == "good":
        tip = bill * .20
    elif service == "fair":
        tip = bill * .15
    elif service == "bad":
        tip = bill * .10
    break
print('Tip amount: %.2f' % tip)
print('Total amount: %.2f' % (tip + bill))
print('Amount per person: %.2f' % ((tip + bill) / split))
"""