def bubblesort(lst):
    print 'Bubble sorting'
    for j in range (0,len(lst)-1):
        for i in range (0,len(lst)-1-j):
            if lst[i]>lst[i+1]:
               lst[i],lst[i+1]=lst[i+1],lst[i]










lst=[4,5,9,1,3,2,7]
print lst
bubblesort(lst)
print(lst)
