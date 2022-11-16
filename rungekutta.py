import math
def f(x,y):
    f = 1+math.pow(y,2)
    return f

def rk(x, y, h):    
    k1 = h*f(x, y)
    k2 = h*f(x+(h/2), y+(k1/2))
    k3 = h*f(x+(h/2), y+(k2/2))
    k4 = h*f(x+h, y+k3)

    k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    y = y+k
    return y

def main():
    x0 = 0
    y0 = 0
    xf = 1.4
    h =  0.1
    while x0 <= xf:
        
        print("x:\t\t", "%.2f" % x0)
        print("y("+"%.2f" % x0+"):\t", "%.5f" % y0)
        y0 = rk(x0, y0, h)
        x0 = x0+h
    print("x:\t\t", "%.2f" % x0)
    print("y("+"%.2f" % x0+"):\t", "%.9f" % y0)

 
main()