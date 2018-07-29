# While Loops and Break Statement
total2 = 0
# While loops don't initialize the index for you (j in this case)
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)
# Finding only the Positive numbers
given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)
given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
    if element <= 0:
        break
    total4 += element
print(total4)
# given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total5 = 0
i = 0
while True:
    total5 += given_list2[i]
    i += 1
    if given_list2[i] <= 0:
        break
print(total5)
# Find the sum of the negative numbers
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total6 = 0
i = 0
while i < len(given_list3):
    if given_list3[i] <= 0:
        total6 += given_list3[i]
    i += 1
print(total6)
