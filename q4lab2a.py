def palindrome(n):
    for i in range(0,int(len(n)/2)):
        if n[i] == n[len(n) - 1 - i]:
            return True
        else:
            return False

x = input("Original number ")
if palindrome(x):
    print("Given number palindrome")
else:
    print("Given number not palindrome")
    
def maximum(a):
    co = a[0]
    for i in range(len(a)):
        if a[i] > co:
            co = a[i]
    return co

m = [4,6,8,24,12,2]
print(maximum(m))