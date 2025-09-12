def solve(s):
    result = []
    
    for i,ch in enumerate(s):
        if i == 0 or s[i-1] == " ":
            result.append(ch.upper())
            
        else:
            result.append(ch)
            
    return "".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
