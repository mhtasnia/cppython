from itertools import product
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    def get_combinations(max_values):
        ranges = [range(0, max_value + 1) for max_value in max_values]
        return list(product(*ranges))
        
    def sum_of_list(lst):
        total = 0
        for num in lst:
            total += num
        return total

    max_values = [x, y, z] 
    combinations = list(get_combinations(max_values))
    
    filtered_combinations=[]
    
    for combination in combinations:
        if sum_of_list(combination) != n:
            filtered_combinations.append(combination)
            
    print([list(t) for t in filtered_combinations])
