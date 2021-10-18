#Digit Product
n = int(input())

product = 1

while n != 0:
    if n % 10 != 0:
        product *= n % 10
    n //= 10

print(product)

#Largest Power of 3
"""Given a natural number N, output the largest integer power of 3 which
does not exceed N."""
N=int(input())
k=0
while 3**k<N:
    M=3**k

    k+=1
print(M)

#Triangle
a=int(input())
b=int(input())
c=int(input())

small=min(a,b,c)
large=max(a,b,c)
med = a+b+c-small-large

if small+med<large:
    print("No Triangle")
elif (small**2+med**2)==(large**2):
    print("Right Triangle")
elif small**2+med**2<large**2:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")



#The Root of the Number
n=int(input())


def root(n):
    root=0
    while n>0:
        root+=n%10
        n=n//10
    return root
    
root_n=root(n)
print(root_n)
while root_n>=10:
    root_n=root(root_n)
    print(root_n)




a=int(input())
b=int(input())
c=int(input())
d== b * b - 4 * a * c

if a==0:
    print("Non-quadratic equation")
    if b==0:
        if c==0:
            print("Infinite solutions")
        else:
            print("No Solutions")
    else:
        print("One solution:",-c/b)
elif d<0:
    print("Quadratic equation","Discriminant:",d,"No Solutions")
else:
    x1=(-b - d**0.5) /( 2 * a)
    x2=(-b + d**0.5) /( 2 * a)
    print("Quadratic equation",x1,x2)
