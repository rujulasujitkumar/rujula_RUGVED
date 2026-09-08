n=int(input("Enter a no."))
s=str(n)
if len(s)<3:
    print("not a hill no.")
else:
    i=1
    while i<len(s) and s[i]>s[i-1]:
        i+=1
    if i==1 or i==len(s):
        print("not hill no")
    else:
        while i<len(s) and s[i]<s[i-1]:
            i+=1
        if i==len(s):
            print("Hill no.")
        else:
            print("Not hill no.")