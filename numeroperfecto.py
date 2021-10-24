n=int(input("Ingresa un numero"))
x=2
perfecto=0
while x<=n:
    if n%x==0:
        perfecto=perfecto+(n/x)
    x=x+1
if perfecto == n:
    print("El numero {0} es perfecto".format(n))
else:
    print("El numero {0} no es perfecto".format(n))