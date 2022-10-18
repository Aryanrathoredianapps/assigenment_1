L= [1,2,3,5]
s= []
for i in range(L[0], L[-1]+1):
    if i not in L:
        s.append(i)
print(s)
