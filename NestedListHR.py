if __name__ == '__main__':
    grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade.append([name, score])
    
    grade.sort(key=lambda x : x[1])
    
    second_low = None
    for i in range(1, len(grade)):
        if grade[i][1] > grade[0][1]:
            second_low = grade[i][1]
            break
    
    output = []
    for i in range(1, len(grade)):    
        if grade[i][1] == second_low:
            output.append(grade[i][0])    
    
    output.sort()
    for i in output:
        print(i)
        
