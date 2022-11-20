#input->1: 434256          Explanation:  4+6=10  3+5=8  4+2=6
#output:   1086                    Ans:      1086

#input->2: 7210654         Explanation:  7+4=11  2+5=7  1+6=7  0
#output:   11770                   Ans:      11770


def closureSum(st):
    n=len(st)
    for i in range(0,n//2):
        print(int(st[i])+int(st[-1-i]),end="")
        
    if n%2!=0:
        print(st[n//2])


s=input("Enter the numbers:\n") 
ans=closureSum(s)

