def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #print(array, target, start, end, mid)
        if array[mid] == target:
             return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] <= target:
            start = mid + 1
        else:
            return None

# 가게 부품 갯수
n = int(input())

# 가게 부품 목록
array = list(map(int, input().split()))
array.sort()

# 손님 확인 할 부품 갯수
m = int(input())
# 손님 확인 할 부품 목록
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
