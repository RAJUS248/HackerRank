if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

# -9 x 7 = -63. 7 is hoursglass summing 7 values -9 is range of matrix -9 to +9
    maxi = -63     
    for i in range(4):
        for j in range(4):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            arr_sum = top + mid + bottom
            
            if arr_sum > maxi:
                maxi = arr_sum
                
    print(maxi)
            
            
