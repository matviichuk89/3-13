import math

a=float(input("Введіть а: "))
b=float(input("Введіть b: "))
c=float(input("Введіть c: "))
k=float(input("Введіть коефіцієнт (k): "))

if a+b>c and a+c>b and b+c>a:
    print("Трикутник існує")
    A=a*k
    B=b*k
    C=c*k
    print(A)
    print(B)
    print(C)

else:
    print("Трикутник не існує")