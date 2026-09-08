#a]Pattern 1
n=int(input("enter n"))
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)


#b]Pattern 2
n=int(input("enter n"))
for i in range(1,n+1):
    st=i
    sp=2*n-2*i-1
    if sp==-1:
        print('*'*(2*i-1))
    else:
        print('*'*st +' '*sp +'*'*st)
for i in range(n-1,0,-1):
    st=i
    sp=2*n-2*i-1
    print('*'*st +' '*sp +'*'*st)