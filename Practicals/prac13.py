import matplotlib.pyplot as plt
import numpy as np
import math

def sine():
    sine=[math.sin(math.radians(i)) for i in range(0,361)]
    plt.plot(sine)
    plt.grid()
    plt.axvline(x=0, color="k")
    plt.axhline(y=0, color="k")
    plt.xlabel("Angles")
    plt.ylabel("Values")
    plt.show()

def cosine():
    sine=[math.cos(math.radians(i)) for i in range(0,361)]
    plt.plot(sine)
    plt.grid()
    plt.axvline(x=0, color="k")
    plt.axhline(y=0, color="k")
    plt.xlabel("Angles")
    plt.ylabel("Values")
    plt.show()

def exp():
    s=[math.exp(i) for i in np.linspace(0,10,100)]
    plt.plot(s)
    plt.grid()
    plt.axvline(x=0, color="k")
    plt.axhline(y=0, color="k")
    plt.xlabel("Angles")
    plt.ylabel("Values")
    plt.show()

def poly():
    p=[]
    s=""
    n=int(input("Enter the highest power: "))
    for i in range(n, -1, -1):
        c=int(input("Enter the coefficient of term with power "+str(i)+":"))
        p.append(c)
        if(c<0):
            if i==0:
                s+=str(c)
                continue
            s+=str(c)+'x^'+str(i)
        elif c==0:
            continue
        else:
            if i==0:
                s+="+"+str(c)
                continue
            s+="+"+str(c)+'x^'+str(i)
    print("Plotting polynomial curve..")

    y=np.array(p)
    pl=[np.polyval(y,x) for x in np.linspace(-10,10,100)]
    plt.grid()
    plt.axvline(x=0, color="k")
    plt.axhline(y=0, color="k")
    plt.xlabel("Angles")
    plt.ylabel("Values")
    plt.plot(pl)
    plt.show()

def main():
    sine()
    cosine()
    exp()
    poly()

if __name__ =="__main__":
    main()
