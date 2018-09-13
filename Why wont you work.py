from pprint import pprint
import traceback
# Work plz.txt = Random letters in a txt file
# First one is not printing but the second is
# First one
try:
    f = open("C:\\Users\\Snows\\Desktop\\Work plz.txt")
    f.readlines()
    f.close()
except:
    pprint(traceback.print_exc())  
# Second one
# f = open("C:\\Users\\Snows\\Desktop\\Work plz.txt")
# for line in f:
#    print(line)
# f.close()
