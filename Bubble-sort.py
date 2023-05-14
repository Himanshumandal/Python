# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
list=[5,4,3,2,1]
n=len(list)
#selection sort
for i in range(n):
    for j in range(n-i-1):
        if list[j]>list[j+1]:
           list[j],list[j+1]=list[j+1],list[j]
            
        
        print(j,list)
    print(i,list)

#print(list)
