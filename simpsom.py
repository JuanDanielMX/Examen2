import math
a = 1/(2*math.pi)
b = 2
x = 2

def expre(x):
    return (math.sin(1/x))

ev1=(2*a+b)/3
ev2=(a+2*b)/3
sum1 = expre(ev1)
sum2 = expre(ev2)

simp = (b-a)/8*(expre(a) + 3*sum1 + 3*sum2 + expre(b))
print(simp)

