num_of_test_case = int(input())
my_list = ['T', 'i', 'm','u','r']
my_list.sort()
for i in range(num_of_test_case):
    len_of_name = int(input())
    name = list(input())
    name.sort()

    if len_of_name != 5:
        print(f"NO")
    else:
        if my_list == name:
            print("YES")
        else:
            print("NO")