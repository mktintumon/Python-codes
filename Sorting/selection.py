def selection(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if(a[j]<a[min]):
                min = j
        a[i], a[min] = a[min], a[i]
            


a = [2,4,1,9,5,10,7]
selection(a)
print(a)