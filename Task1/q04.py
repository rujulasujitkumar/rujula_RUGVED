def selection_sort(s):
    arr=list(s)
    n=len(arr)
    for i in range(n):
        smallest= i
        for j in range(i+1,n):
            if arr[j]<arr[smallest]:
                smallest=j
        arr[i],arr[smallest]=arr[smallest],arr[i]
    return ''.join(arr)
s=input("enter string")
print(selection_sort(s))