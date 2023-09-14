# this is comment in python-- whether one or multiple lines  and even AFTER in a line!

integer1 = 5 # this is a variable named integer1 that we have assigned the value of 5

# TO DO- need to show float data type
float1 =  5.0


# MATH operations:

# ADD   +

added = 4 + 4
print(added)

# Subtract   -

subs = 10 - 5
print(subs)

# Multiply   *

prod = 5 * 10
print(prod)

# Divide   /
# always results in a float
div = 10 / 2
print(div)

# Floor division  //
# results in an integer
floor = 7 // 2
print(floor)

# Modulo  %
# gives us the remainder
# BIG HINT!!!  We'll use this for determining odd/even numbers
rem = 7 % 2
print(rem)

# Exponent  **
power = 2 ** 3
print(power)

#  quick chat about = and ==

integer3 = 3

print(integer3==3)
print(integer3=='3')
print(integer3==int('3'))

# STRINGS
stringy = 'Any kind  of characters !@#$%nhgo9235 inside of quotes?'
# strings are iterable, immuteable, ordered
print(stringy[4])

#concatenation:
stringy1 = 'This'
stringy2 = ' is'
stringy3 = ' not'
stringy4 = ' one word!'

add_str = stringy1 + stringy2 + stringy3 + stringy4
print(add_str)

add_str2 = add_str + " " +'Here\'s another sentence added to the string!'
print(add_str2)

#Interpolation
some_name = 'Andrew'

f_exp = f"This is just another string BUT we can throw in a python variable here --> {integer3}"
print(f_exp)

#Lists
# lists are ordered, muteable, dynamic, iterable
alist = []
alist2 = [1, 2, 3]
print('STUFF ABOUT LISTS:\n')
print(type(alist2), len(alist2))
print(alist2[0])
print(alist2[1])
print(alist2[2])

#.append()  - adds an item to the end of the list  (throwing a book on top of the stack)

alist2.append(4)
alist2.append(4)
print(alist2)

# .pop()   - takes the last element out of the list
# optional parameter is position in list, can also use returned value
popped = alist2.pop(2)
print(alist2)
print(popped)

# .remove()  find the FIRST occurence of a value and remove it from the list

alist2.remove(4)
alist2.remove(4)
print(alist2)

alist2.append(3)
alist2.append(4)
alist2.append(5)
print(alist2)
print("OK we're done with changing the list for now")
print('Range demo: \n\n')
print(list(range(5,10, 2)))


print('\n\nLOOPING:\n')


numbers = list(range(5, 15))


#Loops in python:

# basic for loop

    #syntax -->   for item in items:
for num in numbers:
    wanted_num = num * 10
    print(wanted_num)

# index loop
for i in range(len(numbers)):
    print(i, numbers[i])

# While loop
    # loops while condition is True

while True:
    print("why did'nt I stop this loop")
    break

counter = 0
while counter < 10:
    print(counter)
    counter += 1

l = 0 
r = len(numbers)-1
while l < r:
    print(l)
    l += 1

print('\nMembership checks:\n')

name_list = ['William', 'Zachary', 'Andrew'] 
#Membership checks
# is this value IN that iterable?
print("Andrew" in name_list)
print("Jack" in name_list)
print('back' in 'back to the future' )
print('front' in 'back to the future' )

# Conditionals
# IF/ELIF/ELSE

age = 65
if age <= 0:
    print('condition fired!')
    age +=18


if age >= 65:
    print("you're an Senior")
elif age < 18:
    print("you're a kid!")
else:
    print("you're a Adult")
print(age <= 0)
print(age >= 65)
print(age < 18)

#and / or
# Truth tree
# T and T -->  T
# T and F -->  F
# F and F -->  F

# T or T -->  T
# T or F -->  T
# F or F -->  F

if age < 66 and age > 18:
    print('I told ya it was an ADULT!!!')


def plusfive(num):
    print(num + 5)
def timesfive(num):
    return num * 5

# timesfive(plusfive(5))
# plusfive(timesfive(5))

# x = int(input('what do you wanna type?'))
# print(x, type(x))






def ageism(num):
    if num >= 65:
        print("you're an Senior")
    elif num < 18:
        print("you're a kid!")
    else:
        print("you're a Adult")

y = int(input('gimme an age'))
ageism(y)



















