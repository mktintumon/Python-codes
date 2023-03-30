def insertion(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key
       
            
a = [2,4,1,9,5,10,7]
insertion(a)
print(a)