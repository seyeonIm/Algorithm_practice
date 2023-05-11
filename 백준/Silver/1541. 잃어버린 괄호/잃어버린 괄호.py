import sys
# 50-30+60-20
# (-)기호부터 다음 (-)전까지
arr = input().split('-')
# arr = ' '.join(arr).split()
# print(arr)
num = []
# arr [50, 30+60, 20] string

for elements in arr:
    subsum = 0
    element_arr = elements.split('+')
    for ele in element_arr:
        subsum += int(ele)
    num.append(subsum)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

