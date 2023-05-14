# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
list=[5,4,3,2,1]
n=len(list)
#selection sort
for i in range(n):
    min=i
    for j in range(n):
        if list[min]<list[j]:
            min=j
            
        list[min],list[i]=list[i],list[min]
        print(j,list)
    print(i,list)

#print(list)
