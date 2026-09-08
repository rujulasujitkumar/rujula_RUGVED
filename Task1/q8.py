s=input("enter string")
n=int(input("enter n"))
if len(s)%n!=0:
    print("not possible")
else:
    p1=s[:n]
    p2=[]
    check=True
    for i in range(0,len(s),n):
        u=s[i:i+n]
        p2.append(u)
        if u!=p1:
            check=False
    if check==False:
        print("seqence cant be szme")
    else:
        for p in p2:
            print(p,end=",")

