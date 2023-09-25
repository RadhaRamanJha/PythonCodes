# Method 1 --- By using Split method
input_list = input('Enter elements of a list of numbers separated by space :')
print("\n")
user_list = input_list.split()
# print list
print('list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
      # convert each item to int type
    user_list[i] = int(user_list[i])
    print(user_list[i])