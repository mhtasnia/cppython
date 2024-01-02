import math
from functools import reduce


def gcd_of_list(numbers):
    return reduce(math.gcd, numbers)


n, q = map(int, input().split())
list_of_vector = list(map(int, input().split()))
for i in range(q):
    list_of_query = list(map(int, input().split()))

    if list_of_query[0] == 2:
        z = gcd_of_list(list_of_vector[list_of_query[1]:list_of_query[2]])

    if list_of_query[0] == 1:
        for j in range(list_of_query[1] - 1, list_of_query[2]):
            list_of_vector[j] += list_of_query[3]
