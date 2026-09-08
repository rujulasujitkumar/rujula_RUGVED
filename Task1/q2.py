s=input("Enter string")
s1=''.join(sorted(s))
print("Sorted:",s1)
count={}
for i in s1:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i,j in count.items():
    print(i,"=",j)