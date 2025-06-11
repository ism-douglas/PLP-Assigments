my_list = [1,"Python",3,4,5]
print("Before append",my_list)
my_list.append(36)
print("After append",my_list)

their_list = [6,8,13,"Laravel"]
print(their_list)

my_list.extend(their_list)
print("List after extend",my_list)

