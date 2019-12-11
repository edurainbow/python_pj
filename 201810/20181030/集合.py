#__author:"Peter"
#date:2018/10/30

# s = set('alex li')
# print(s)

a = set([1,2,3,4,5])
b = set([4,5,6,7,8])
print(a.intersection(b)) #{4, 5} 交集
print(a & b)
print(a.union(b)) #{1, 2, 3, 4, 5, 6, 7, 8}并集
print(a | b)
print(a.difference(b)) #{1, 2, 3}差集
print(a-b)
print(a.symmetric_difference(b))#{1, 2, 3, 6, 7, 8}
print(a^b)
print(a.issuperset(b)) #父集
print(a>b)
print(a.issubset(b))#子集
print(a<b)