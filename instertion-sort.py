# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
list=[5,4,3,2,1]
n=len(list)
#selection sort
for i in range(1,n):
    temp=list[i]
    j=i-1
    while j>=0 and temp<list[j]:
        list[j+1]=list[j]
        j-=1
    list[j+1]=temp
    #print(j,list)
    print(i,list)

#print(list)
