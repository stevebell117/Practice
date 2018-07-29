wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
print(wizard_list)
wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)
print(wizard_list[2])
wizard_list[2] = 'snail tongue'
print(wizard_list)
# Writing 2:5 = Show the items from index position 2 up to (but not including) index position 5
print(wizard_list[2:5])
some_numbers = [1, 2, 5, 10, 20]
some_strings = ['Which', 'Witch', 'Is', 'Which']
numbers_and_strings = ['Why', 'was', 6, 'afraid', 'of', 7, 'beacuse', 7, 8, 9]
print(numbers_and_strings)
wizard_list.append('bear burp')
print(wizard_list)
# Append adds an item to the end of a list
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)
# del (short for delete)
del wizard_list[5]
print(wizard_list)
del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)
# List Arithmetic (Adding list)
list1 = [1, 2, 3, 4]
list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
print(list1 + list2)
list1 = [1, 2, 3, 4]
list2 = ['I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
list3 = list1 + list2
print(list3)
list1 = [1, 2]
print(list1 * 5)
# tuples = like a list that uses parentheses (cannot change once you've created it)
fibs = (0, 1, 1, 2, 3)
print(fibs[3])
#Map also referred to as a dict (Short for dictionary)
favorite_sports = ['Ralph Williams, Football',
                'Michael Tippett, Basketball',
                'Edward Elgar, Baseball',
                'Rebecca Clarke, Netball',
                'Ethel Smyth, Badminton',
                'Frank Bridge, Rugby']
favorite_sports = {'Ralph Williams' : 'Football',
                'Michael Tippett' : 'Basketball',
                'Edward Elgar' : 'Baseball',
                'Rebecca Clarke' : 'Netball',
                'Ethel Smyth' : 'Badminton',
                'Frank Bridge' : 'Rugby'}
print(favorite_sports['Rebecca Clarke'])
del favorite_sports['Ethel Smyth']
print(favorite_sports)
favorite_sports['Ralph Williams'] = 'Ice Hockey'
print(favorite_sports)
# Python for Kids Pg 42 Puzzles
X = (3 * 25) + 80
print(X)
First = 'Bob'
Last = 'Zer'
print('Hi There, %s %s!' % (First, Last))