'''generating random captha list'''
import random
captha_list = []
for i in range (0,32):
    captha_list.append(random.randint(100000,999999))
print(captha_list)
