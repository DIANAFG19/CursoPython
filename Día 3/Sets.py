mi_set = set([1,2,3,4,5]) #set({1,2,3,4,5})    #set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,4,5}
print(type(otro_set))
print(otro_set)

print(len(mi_set))

print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.remove(3)
print(s1)

s1.discard(5)
print(s1)

sorteo = s1.pop()
print(sorteo)

s1.clear()
print(s1)
