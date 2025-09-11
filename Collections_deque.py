from collections import deque
N = int(input())
op = deque()
for i in range(N): 
    arr = input().split()
    if arr[0] == "append":
        op.append(arr[1])
        

    elif arr[0] == "appendleft":
        op.appendleft(arr[1])
        

    elif arr[0] == "pop":
        op.pop()
        

    elif arr[0] == "popleft":
        op.popleft()

print(*op)
