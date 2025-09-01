n = int(input())
phonebook = {}

for _ in range(n):
    name,number = input().split()
    phonebook[name] = number

while True:
    try:
        quarry = input().strip()
        if quarry in phonebook:
            print(f"{quarry}={phonebook[quarry]}")

        else:
            print("Not found")
            
    except EOFError:
        break
        
