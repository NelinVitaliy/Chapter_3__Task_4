
# l = [1,2,3,5,7,8,12,14]
# m = range(1,len(l))
# min(set(m)-set(l))


l = [1, 14, 2, 5, 3, 7, 8, 12]
# l = input('Enter you number: ')
# l = list[l]
# print(type(l))
for i in range(1, max(l)):
    if i not in l : break
print('You lost number: ' + str(i))