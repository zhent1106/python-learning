set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
# 交集，并集，差集，对称差运算
print(set1 & set2)
print(set1.intersection(set2))
print(set1 | set2)
print(set1.union(set2))
print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
print(set2.issubset(set1))
print(set3 <= set1)
print(set3.issubset(set2))
print(set1 >= set2)
print(set1.issubset(set2))
print(set1 >= set3)
print(set2.issubset(set3))
