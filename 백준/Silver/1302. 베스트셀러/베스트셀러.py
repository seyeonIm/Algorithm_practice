N = int(input())
titleOfBooks = list()
dict = {}
BestSellerlist = []

for i in range(N):
    book = input()
    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1

num = max(dict.values())

for i in dict:
    if dict[i] == num:
        BestSellerlist.append(i)

BestSellerlist.sort()
print(BestSellerlist[0])