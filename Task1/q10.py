#self-note:
#Luhn Algorithm:A method used to check whether a number is valid by following a simple mathematical calculation
#It is mainly used to check numbers like credit card numbers and detect typing mistakes
#1.Start from the rightmost digit
#2.Move left
#3Double every second digit
#4.If the doubled value is greater than 9,subtract 9
#5.Add all the digits
#6.If the total is divisible by 10,the number is valid 

def luhn_algo(n):
    s=str(n)
    total=0
    co=0
    for i in range(len(s)-1,-1,-1):
        dig=s[i]
        if co%2==1:
            dig=dig*2
            if dig>9:
                dig=dig-9
        total=total+dig
        co=co+1
    if total%10==0:
        print("valid no.")
    else:
        print("invalid no.")

n=input("enter credit card no.")
luhn_algo(n)
