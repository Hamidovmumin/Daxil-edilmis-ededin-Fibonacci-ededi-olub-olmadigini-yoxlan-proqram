#============================== Daxil edilmiş ədədin Fibonacci ədədi olub olmadığını yoxlamaq =========================#
def Fibonacci_ededi(n):
    if(n<0):
        return False
    a,b=0,1
    while(b<n):
        a,b=b,a+b
    return b==n

eded=int(input('Ədədi daxil edin:'))

if(Fibonacci_ededi(eded)):
    print(f'{eded} Fibonacci ədədidir')
else:
    print(f'{eded} Fibonacci ədədi deyil ')
