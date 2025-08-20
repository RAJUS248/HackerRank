if __name__ == '__main__':
    N = int(input())
    
    lst = []
    
    for _ in range(N):
        cmd_list = input().strip().split()
        cmd = cmd_list[0]
        
        if cmd == 'insert':
            i = int(cmd_list[1])
            e = int(cmd_list[2])
            lst.insert(i,e)
            
        if cmd == 'print':
            print(lst)
            
        if cmd == 'remove':
            i = int(cmd_list[1])
            lst.remove(i)
            
        if cmd == 'append':
            i = int(cmd_list[1])
            lst.append(i)
            
        if cmd == 'sort':
            lst.sort()
            
        if cmd == 'pop':
            lst.pop()
            
        if cmd == 'reverse':
            lst.reverse()
        

"""
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""
