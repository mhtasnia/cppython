if __name__ == '__main__':
    N = int(input())
    commands = [] 
    my_list = []
    for i in range(N):  # Corrected range: 0 to N-1 
        inputs = input() 
        commands.append(inputs.split()) 

    
    for command in commands:
        if command[0] == 'insert':
            index = int(command[1])
            element = int(command[2])
            my_list.insert(index, element)
            
        if command[0] == 'append':
            element = int(command[1])
            my_list.append(element)
         
        if command[0] == 'remove':
            element = int(command[1])
            my_list.remove(element)  
            
        if command[0] == 'pop':
            my_list.pop() 
        
        if command[0] == 'sort':
            my_list.sort() 
            
        if command[0] == 'reverse':
            my_list.reverse() 
            
        if command[0] == 'print':
            print(my_list)
        
