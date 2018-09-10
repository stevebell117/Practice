# Using for loops
for x in range(0, 5):
    print('Hello')
print(list(range(10, 20)))
for x in range(0, 5):
    print('hello %s' % x)
wizard_list = ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
for i in wizard_list:
    print(i)
hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print(i)
    print(i)
hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)
# 20 found coins plus 10 magic coins multiplied by 365 minus 3 coins a week stolen and 52 weeks in a year
20 + 10 * 365 - 3 * 52
found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1,53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week, coins))
# While we're talking about looping
# A for loop is a loop of specific length whereas a while loop is a loop that is used when you don't know ahead of time when it needs to stop looping
for step in range(0, 20):
    print(step)
# This is for a basic example of a while loop
# step = 0
# while step < 10000:
#    print(step)
#    if tired == True:
#        break
#    elif badweather == True:
#        break
#    else:
#        step = step + 1
x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)
# Another common use of the while loop is to create semi-eternal loops. This could go on forever, but actually continues until something happens in the code to break out of it.
# while True:
#   lots of code here
#   lots of code here
#   lots of code here
#   if some_value == True:
#       break
# The Hello Loop
# will do it once then break
for x in range(0, 20):
    print('Hello %s' % x)
    if x < 9:
        break
# Even numbers
for x in range(2, 16, 2):
    print(x)
# My five favorite ingredients
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']
x = 1
for i in ingredients:
    print('%s %s' % (x, i))
    x = x + 1
# Your weight on the Moon
weight = 200
for year in range(1, 16):
    weight = weight + 1
    moon_weight = weight * 0.165
    print('Year %s is %s' % (year, moon_weight))