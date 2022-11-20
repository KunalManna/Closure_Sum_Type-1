#input----434256          Explanation:  4+6=10  3+5=8  4+2=6
#output---1086                    Ans:      1086


def closureSum(st):
    n=len(st)
    for i in range(0,n//2):
        print(int(st[i])+int(st[-1-i]),end="")


s=input("Enter the numbers:\n") 
ans=closureSum(s)

