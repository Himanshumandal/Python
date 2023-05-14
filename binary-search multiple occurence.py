# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
list=[1,2,2,4,5,5,5,6,7,7,8,9,50,52,54]
n=len(list)
#Binary Search
st=0
mid=0
end=n-1
key=5
while st<end :
    mid=st+(end-st)//2
    if list[mid]==key :
       ind=mid
       st=mid+1
       end=mid
       
    elif list[mid]<key:
       ## print(st,"start increament from mid")
        st=mid+1
    else :
        #print(end,"end is decreament from mid")
        end=mid-1
print(st,"find occurance")
print(end,"find occurance")
