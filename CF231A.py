num_of_test_case = int(input())
sub_count = 0
for i in range(num_of_test_case):
    a, b, c = map(int, input().split())
    sure_list = [a, b, c]
    if sure_list.count(1) >= 2:
        sub_count = sub_count + 1
print(sub_count)
