from typing import AbstractSet
from matplotlib import interactive
import numpy as np
from math import tan, pi
import matplotlib.pyplot as plt
from numpy.core.arrayprint import format_float_scientific
# Variant 6
# y = tg(x)
from math import cos, tan
import copy

h = 0.1
n = int(2 / h) + 1 # отрезок длины 2 с шагом h [-1,1]
# x = list()
    # x.append(-1)
    # for i in range(1,n):
    #     tmp = x[i-1] + h
    #     x.append(tmp)
x = [-1.0, -0.9, -0.8, -0.7, 
    -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 
    0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

def f(x):
    return tan(x)


def F(x, y):
    return (1 - x**2) * y + 1/(cos(x)**2) - (1 - x**2) * tan(x)

def RK_meth():
    y = list()
    y.append(f(-1))
    for i in range(n-1):
        k1 = h * F(x[i],y[i])
        k2 = h * F(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * F(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * F(x[i] + h, y[i] + k3)
        y_next = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        y.append(y_next)
    plt.plot(x,y,"ro-")
    plt.title("RK_method")    
    plt.show()
    return y


def AB_meth(y):
    for i in x:
        print(i)
    yy = list()
    yy = copy.copy(y)
    for i in range(3, n-1):
        tmp = y[i] + (h/24) * (55 * F(x[i], y[i]) - 59 * F(x[i-1], y[i-1]) 
        + 37 * F(x[i-2], y[i-2]) - 9 * F(x[i-3], y[i-3]))
        yy[i+1] = tmp

    plt.plot(x,yy,"ro-")
    plt.title("AB_method")    
    plt.show()
    return yy

def errors(y, name):
    # calculate tg(x_i):
    teoretical_values = list()
    for i in x:
        teoretical_values.append(f(i))

    print(f'------------\nError for {name}')
    Y = []
    for j in range(len(y)):
        err = abs(teoretical_values[j] - y[j])
        print(f'\t{err}')
        Y.append(err)

    plt.plot(x, Y, "ro-")
    plt.title(f"Error. {name}")
    plt.show()

    return Y


def output_values(lst, name):
    print(f'-------------------------\nValue of {name}:')
    j = 1
    for i in lst:
        print(f'\t{i}')
        j += 1
    

def output_teoretical_value_table():
    for i in x:
        print(f'\t{f(i)}')

    


def main():
    y_rk = RK_meth()
    y_ab = AB_meth(RK_meth())

    plt.title("Value for RK_meth and AB_meth")
    plt.plot(
        x, y_rk, "ro-",
        x, y_ab, "bo-"
    )
    plt.show()

    e_rk = errors(RK_meth(), RK_meth.__name__)
    e_ab = errors(AB_meth(RK_meth()), AB_meth.__name__)

    plt.plot(
        x, e_rk, "ro-",
        x, e_ab, "bo-"
    )
    plt.title("Error for RK_meth and AB_meth")
    plt.show()

    output_teoretical_value_table()
    output_values(RK_meth(), RK_meth.__name__)
    output_values(AB_meth(RK_meth()), AB_meth.__name__)
    errors(RK_meth(), RK_meth.__name__)
    errors(AB_meth(RK_meth()), AB_meth.__name__)


    return 0





if __name__ == "__main__":
    main()

