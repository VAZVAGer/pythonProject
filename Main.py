

def fun(n,k):
    if n >20:
        return (0)
    elif n<=20:
        total4=0
        for l in range (1,n+1):
            if l%2==0:
                total4=total4+l**k
        return(total4)
a=fun(20,20)

print(a)