n = 17
width = len(bin(n)) - 2
for i in range(1,n+1):
    dec = str(i).rjust(width)
    octal = oct(i)[2:].rjust(width)
    hexa = str(hex(i)).upper()[2:].rjust(width)
    binary = bin(i)[2:].rjust(width)
    print(dec,octal,hexa,binary)
