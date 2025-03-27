Task1:

def factorial (x):
    if x <=1:
        return 1
    else:
        return x * factorial(x-1)
        
if __name__ =="__main__":
    num = 4
    print(f"THE FACTORİAL OF {num} is {factorial(num)}")
    
Task:2
    
    from math import pi
sine_term = lambda x, a: ((-1)**a) * (x**(2*a + 1)) / factorial(2*a + 1)

def sine_x(x, n):
    
    x = x * pi / 180  
    total = 0
    for a in range(n):
        total += sine_term(x, a)
    return total

x = float(input("\n2. enter x angle(degree) : "))
n = int(input("total term: "))
print(f"sin({x}) ≈ {sine_x(x, n)}")

Task3:

total = 0 
def quest2(n):
    global total
    if n == 0:
        return
    total += 1 / n 
    quest2(n - 1)
n = int(input("\n Enter a value: "))
quest2(n)
print(f"Total is : {total}")
