n = int(input())
for i in range(n):
    x, y, z = input().split()
    list_made = [x, y, z]
    list_of_num = [int(item) for item in list_made]
    list_of_num = sorted(list_of_num)
    if list_of_num[2] == list_of_num[0] + list_of_num[1]:
        print("YES")
    else:
        print("NO")
