
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b = b,a+b
    return(a)
    
for n in range(1,10):
    print(fib(n))