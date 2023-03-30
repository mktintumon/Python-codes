def bubble(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1):
            if(a[j+1]<a[j]):
                a[j], a[j + 1] = a[j + 1], a[j]
            


a = [2,4,1,9,5,10,7]
bubble(a)
print(a)