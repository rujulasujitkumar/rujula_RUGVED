#self-note (Coleman-Liau formula)-It gives us an idea of how difficult/easy the text is to read
#Take the text as input
#Count the total number of letters
#Count the total number of words
#Count the total number of sentences
#Calculate L: L=(letters\words)*100
#Calculate S: S =(sentences\words)*100
#Use the main formula: Index=0.0588*L-0.296*S-15.8
#Print the Index as the grade level

text=input("enter text")
letters=0
for i in text:
    if i.isalpha():
        letters+=1

words=0
s=text.split()
for i in s:
    words+=1
    
sentences = 0
for i in text:
    if i=="." or i=="!" or i=="?":
        sentences+=1

L = (letters / words)*100
S = (sentences / words)*100
index=(0.0588 * L)-(0.296 * S)-15.8
print("Grade level:", round(index))
