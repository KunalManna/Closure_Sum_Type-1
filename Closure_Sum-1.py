def closureSum(st):
    n=len(st)
    for i in range(0,n//2):
        print(int(st[i])+int(st[-1-i]),end="")


s=input("Enter the numbers:\n") 
ans=closureSum(s)

