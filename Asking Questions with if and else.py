age = 13
if age > 20:
    print('You are too old!')
# A block is a group of programming statemets
age = 25
if age > 20:
    print('You are too old!')
    print('Why are you here?')
    print('Why aren\'t you mowing a lawn or sorting papers?')
# Conditions help us compare things
age = 10
if age >= 10:
    print('You are too old for my jokes!')
age = 10
if age == 10:
    print('What\'s brown and sticky? a stick!!')
# If-then-else statements
print("Want to hear a dirty joke?")
age = 8
if age == 12:
    print("A pig fell in the mud!")
else:
    print("Shh. It's a secret.")
# If and elif statements
age = 12
if age == 10:
    print("What do you call an unhappy cranberry?")
    print("A blueberry!")
elif age == 11:
    print("What did the green grape say to the blue grape?")
    print("Breathe! Breathe!")
elif age == 12:
    print("What did 0 say to 8?")
    print("Hi guy!")
elif age == 13:
    print("Why wasn't 10 afraid of 7?")
    print("Because rather than eating 9, 7 8 pi.")
else:
    print("Huh?")
# Combining conditions by using "and" "or"
if age == 10 or age == 11 or age == 12 or age == 13:
    print("What is 13 + 49 + 84 + 155 + 97? A Headache!")
else:
    print('Huh?')
if age >= 10 and age <= 13:
    print('What is 13 + 49 + 84 + 155 + 97? A headache!')
else:
    print('Huh?')
# Variables with no value-none
myval = None
print(myval)
myval = None
if myval == None:
    print("The variable myval doesn't have a value")
# The difference Between strings and numbers
# Compare the value of the variable "age"
if age == 10:
    print("What's the best way to speak to a monster?")
    print("From as far away as possible!")
# Set the variable "age" to 10
age = 10
if age == 10:
    print("What's the best way to speak to a monster?")
    print("From as far away as possible!")
# Set the "age" to the string '10'
age = '10'
if age == 10:
    print("What's the best way to speak to a monster?")
    print("From as far away as possible!")
# Can turn strings into numbers and numbers into strings with "int" and "str"
age = '10'
converted_age = int(age)
# To convert a number into a sting use "str"
age = 10
converted_age = str(age)
age = '10'
converted_age = int(age)
if converted_age == 10:
    print("What's the best way to speak to a monster?")
    print("From as far away as possible!")
# If you convert a number with a decimal you'll get an error because "int" expects an integer
# To fix this use "float" The "float" function can handle numbers that aren't integers
age = '10.5'
converted_age = float(age)
print(converted_age)
# Programming Puzzles 
# 1 Are you rich?
# Will print I'm rich!!
money = 2000
if money > 1000:
    print("I'm rich!!")
else:
    print("I'm not rich!!")
    print("But I might be later...")
# 2 Twinkies
twinkies = 501
if twinkies < 100 or twinkies > 500:
    print("Too few or too many")
# 3 Just the right number
money = None
money = 1001
if (money >= 100 and money <= 500) or (1001 >= 1000 and 1001 <= 5000):
    print('amount is between 100 & 500 or between 1000 & 5000')
# I can't fight those ninjas
# Create an if statement that prints the string “That’s too many” if the variable ninjas contains a number that’s less than 50, prints “It’ll be a struggle, but I can take ’em” if it’s less than 30, and prints “I can fight those ninjas!” if it’s less than 10. You might try out your code with: ninjas = 5
ninjas = 5
if ninjas < 10:
    print("I can fight those ninjas!")
elif ninjas < 30:
    print("It'll be a struggle, but I can take 'em")
elif ninjas < 50:
    print("That's too many")