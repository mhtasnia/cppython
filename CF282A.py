num_of_test_case = int(input())
initial_num = 0
for i in range(num_of_test_case):
    x = input()
    if x == "X++" or x == "++X":
        initial_num = initial_num + 1
    elif x == "X--" or x == "--X":
        initial_num = initial_num - 1

print(initial_num)
