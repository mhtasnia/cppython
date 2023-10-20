import math
num_of_test_case = int(input())

for i in range(num_of_test_case):
    flat_no, num_of_flat_each_floor = map(int, input().split())
    if flat_no == 1 or flat_no == 2:
        print(1)
    else:
        floor_no = math.ceil((flat_no - 2) / num_of_flat_each_floor) + 1
        print(floor_no)
    