listA = [1,4,2,2,56,4,8,3,3,2]
listA.sort()
ans = []
ans.append(listA[0])

for x in range(1,len(listA)):
    if listA[x] == listA[x-1] and listA[x] not in ans:
        ans.append(listA[x])

print(listA)
print(ans)