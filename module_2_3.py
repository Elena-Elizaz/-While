my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initial_value = 0
print(my_list)
while initial_value < len(my_list):
    count = my_list[initial_value]
    initial_value = initial_value + 1
    if count == 0:
        continue
    elif count < 0:
         break

    else:
        print(count)

