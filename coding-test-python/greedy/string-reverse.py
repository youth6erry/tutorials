#문자열뒤집기
data = input()

#data를 array로 만들기

#초기화
count0 = 0
count1 = 0
#01010010

# 첫번째, 두번째 자리가 다른경우 세팅
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

#첫번째 값 세팅하기
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if '1' == data[i+1]:
            count0 += 1
        else:
            count1 += 1

print(count0, count1)