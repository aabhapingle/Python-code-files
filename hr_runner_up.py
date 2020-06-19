if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr)
    #print(arr)
    i=len(arr)
    for i in range(len(arr)-1, -1, -1):
        if arr[len(arr)-1] > arr[i]:
            print(arr[i])
            break
    else:
        print(arr[len(arr) - 1])

