def caesars_cipher(s, n):
    result=""
    for i in s:
        result=result+chr(ord(i)+n)
    return result

s=input("enter string")
n=int(input("enter shift"))
print("enter encrypted string",caesars_cipher(s,n))