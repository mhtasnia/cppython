x = list(input())
list_of_num = [x[i] for i in range(len(x))if i % 2 == 0]
list_of_num = '+'.join(sorted(list_of_num))
print(list_of_num)
