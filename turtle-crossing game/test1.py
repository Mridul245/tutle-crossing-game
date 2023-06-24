n = int(input())
arr = list(map(int, input().split()))
count = 1

for i in range(0,len(arr)):
    if arr[i] != -1:
        for j in range(0, len(arr)):
            if arr[i] == arr[j]:
                arr[j] = -1
                count += 1
    else:
        continue
    if count == 3:
        continue
    else:
        print(arr[i])
