def anagram_check(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        if(sorted(s1)==sorted(s2)):
            print("Anagram")
        else:
            print("not anagram.")


s1=input("enter string")
s2=input("enter string")
anagram_check(s1,s2)
