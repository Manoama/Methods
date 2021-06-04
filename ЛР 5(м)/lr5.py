from matplotlib import interactive
import numpy as np
from math import tan, pi
import matplotlib.pyplot as plt
from numpy.core.arrayprint import format_float_scientific

# My function : 
#     x * tg(x)

# Interval :
#     [-pi/3; pi/3]


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def f(x):
    return x * tan(x)


# define nodes evenly
def get_interpolar_nodes(interval, num_of_nodes):
    s = 0
    nodes = []
    inter_len = abs(interval[1] - interval[0])
    step = inter_len/ (num_of_nodes - 1)
    nodes.append(interval[0])
    # nodes.append(interval[0] + step)

    for i in range(1, num_of_nodes):
        nodes.append(nodes[i-1] + step)
    return nodes


#Table of f-value in interpolar nodes
def value_table(nodes):
    table = dict()
    for x in nodes:
        table[x] = f(x)
    

    i = 1

    print('-----------------------------')
    print('X                           f(X)\n')
    for key, val in table.items():
        # print(f'x_{i} = {key}   f(x_{i}) = {val}')
        print(f'{key} {val}')
        i += 1
    return table


def Ln_view(table):
    L = "" 
    numerator = ""
    denominator = ""
    k = 0
    print('--------------------------------------\nLn(x) = ')
    for key_k, y_k in table.items():
        numerator = ""
        denominator = ""
        i = 0
        if k == 0:
            print(f'{y_k}*')
        else:
            print(f' + {y_k}*')
        for key_i in table.keys():
            if i != k:
                if key_i < 0:
                    numerator += f'(x+{abs(key_i)})'
                else:
                    numerator += f'(x-{key_i})'
                if key_i < 0:
                    denominator += f'({key_k} + {abs(key_i)})'
                else:
                    denominator += f'({key_k} - {key_i})'
                i += 1
            else:
                i += 1
        k += 1
        print(f'[{numerator}] / [{denominator}]')
        L = f'[{numerator}] / [{denominator}]'
    print(L)
    

def Ln_x(table, x):
    i = 0
    k = 0
    L = 1.0
    numer = 1
    denom = 1
    res = 0
    for x_k, y_k in table.items():
        i = 0
        for x_i in table.keys():
            if i != k:
                # print(f'\nx_k = {x_k}\n x_i = {x_i}')
                L *= (x - x_i)/(x_k - x_i)
                i += 1
            else:
                i += 1
        k += 1
        res += L * y_k
        L = 1.0
    
    return res


def Ln_x_table(table, x):
    Ln_X = list()
    for x in table.keys():
        Ln_X.append(Ln_x(table,x))
    return Ln_X



def splain(table):
    h = list()
    a = list()
    X = list()
    Y = list()
    for k in table.keys():
        X.append(k)

    space = len(X) - 1
    for v in table.values():
        Y.append(v)


    for y in Y:
        a.append(y)
    
    for i in range(space):
        h.append(X[i + 1] - X[i])
    
    V = list()
    V.append(0)
    for i in range(1,space - 1):
        n1 = (Y[i + 1] - Y[i]) / h[i]
        n2 = (Y[i] - Y[i - 1]) / h[i - 1]
        formula = 3 * (n1 - n2)
        # print(formula)
        V.append(formula) 
    V.append(0)

    print(f'--------------------\nV = ')
    for x in V:
        print(f'\t{x}')

    # Define matrix filled "0" 
    A = []
    for i in range(space):
        tmp_lst = list()
        for j in range(space):
            tmp_lst.append(0)
        A.append(tmp_lst)

    for i in range(1, space-1):
        for j in range(space-1):
            if i - j == 1:
                A[i][j] = h[j]
            if i == j:
                A[i][j] = 2*(h[j] + h[j + 1])
            if j - i == 1:
                A[i][j] = h[i]
    A[0][0] = 2 * (h[0] + h[1])
    A[0][1] = h[1]

    A[space - 1][space - 1] = 2 * (h[space - 2] + h[space - 1])
    A[space - 1][space - 2] = h[space - 1]

    for i in range(len(A)):
        print(A[i])

    # Solve AC = V for C .
    A = np.array(A)
    b = np.array(V)
    C = np.linalg.solve(A, b)
    print(f'--------------------\nX = ')
    for x in C:
        print(f'\t{x}')
    
    #b_i:
    B = list()
    for i in range(space - 1):
        n1 = (Y[i + 1] - Y[i]) / h[i]
        n2 = h[i]* (2*C[i] + C[i + 1]) / 3
        formula = n1 - n2
        B.append(formula)

    B.append(((Y[space - 1]- Y[space - 2]) / h[space - 1]) - (2 * h[space - 1] * C[space - 1] / 3))

    print(f'--------------------\nB = ')
    for x in B:
        print(f'\t{x}')

    #d_i:
    D = list()
    for i in range(space - 1):
        formula = (C[i + 1] - C[i]) / (3 * h[i])
        D.append(formula)
    
    D.append( - (C[space - 1]) / (3 * h[space - 1]) )

    print(f'--------------------\nD = ')
    for x in D:
        print(f'\t{x}')

    S = []
    for i in range(space):
        yy = Y[i]
        bb = B[i]
        c = C[i]
        d = D[i]
        S.append([yy, bb, c, d])
    
    print("S(x) = ")
    for i in range(space):
        print(f'\tS{i+1} = \t{toFixed(S[i][0],6)}\t{toFixed(S[i][1],6)}\t{toFixed(S[i][2],6)}\t{toFixed(S[i][3],6)}')
            
    return S


def graphic_Ln_x(table, x):
    X = table.keys()
    Ln_X = Ln_x_table(table, x)

    plt.plot(X, Ln_X, 'ro-')

    XX = list()
    for x in X:
        XX.append(x)
    for i in range(len(XX)):
        dot = f'({toFixed(XX[i],4)}, {toFixed(Ln_X[i],4)})'
        plt.annotate(dot, (XX[i],Ln_X[i]))
    enter = input("Tap 'Enter' to output the graphic Pn(x)\n> ")
    plt.show()


def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {ord}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y




#S_i(x) = a_i + b_i * (x - x_i) + c_i * (x - x_i)^2 + d_i * (x - x_i)^3
def graphic_splain(table, S, x):
    Splain_value = list()
    
    interval = [-pi/3,pi/3]
    num_of_nodes = 12
    s = 0
    nodes = []
    inter_len = abs(interval[1] - interval[0])
    step = inter_len/ (num_of_nodes - 1)
    nodes.append(interval[0])

    for i in range(1, num_of_nodes):
        nodes.append(nodes[i-1] + step)


    interval1 = np.linspace(nodes[0], nodes[1], 10)
    interval2 = np.linspace(nodes[1], nodes[2], 10)
    interval3 = np.linspace(nodes[2], nodes[3], 10)
    interval4 = np.linspace(nodes[3], nodes[4], 10)
    interval5 = np.linspace(nodes[4], nodes[5], 10)
    interval6 = np.linspace(nodes[5], nodes[6], 10)
    interval7 = np.linspace(nodes[6], nodes[7], 10)
    interval8 = np.linspace(nodes[7], nodes[8], 10)
    interval9 = np.linspace(nodes[8], nodes[9], 10)
    interval10 = np.linspace(nodes[9], nodes[10], 10)
    interval11 = np.linspace(nodes[10], nodes[11], 10)
    plt.plot(
        interval1, PolyCoefficients(interval1, [S[0][0], S[0][1], S[0][2], S[0][3]]), '--',
        interval2, PolyCoefficients(interval2, [S[1][0], S[1][1], S[1][2], S[1][3]]), '--',
        interval3, PolyCoefficients(interval3, [S[2][0], S[2][1], S[2][2], S[2][3]]), '--',
        interval4, PolyCoefficients(interval4, [S[3][0], S[3][1], S[3][2], S[3][3]]), '--',
        interval5, PolyCoefficients(interval5, [S[4][0], S[4][1], S[4][2], S[4][3]]), '--',
        interval6, PolyCoefficients(interval6, [S[5][0], S[5][1], S[5][2], S[5][3]]), '--',
        interval7, PolyCoefficients(interval7, [S[6][0], S[6][1], S[6][2], S[6][3]]), '--',
        interval8, PolyCoefficients(interval8, [S[7][0], S[7][1], S[7][2], S[7][3]]), '--',
        interval9, PolyCoefficients(interval9, [S[8][0], S[8][1], S[8][2], S[8][3]]), '--',
        interval10, PolyCoefficients(interval10, [S[9][0], S[9][1], S[9][2], S[9][3]]), '--',
        interval11, PolyCoefficients(interval11, [S[10][0], S[10][1], S[10][2], S[10][3]]), '--',
        
        
        
        )
    plt.show()


    for i in range(len(S)):
        x = np.linspace(-pi/3, pi/3, 10)
        coeffs = [S[i][0], S[i][1], S[i][2], S[i][3]]        
        plt.plot(x, )
        plt.title(f'S_{i}(x)')
        plt.xlabel('X')
        plt.ylabel('S(x)')
        plt.show()

    #     Splain_value.append(S_i)

    # plt.plot(X, Splain_value, 'ro-')

    # for i in range(len(X)):
    #     dot = f'({toFixed(X[i],4)}, {toFixed(Splain_value[i],4)})'
    #     plt.annotate(dot, (X[i],Splain_value[i]))
    # enter = input("Tap 'Enter' to output the graphic Pn(x)\n> ")
    # plt.show()    








def main():
    a = - pi/3
    b = pi/3
    interval = (a,b)
    n = 12
    # n = int(input('\nInput a number of nodes\n> '))
    nodes = get_interpolar_nodes(interval, n)

    val_table = value_table(nodes)
    Ln_view(val_table)
    x = 0.2
    # x = float(input('\nInput the value from [-pi/3; pi/3]\n> '))
    print(f'------------\nLn({x}) = {Ln_x(val_table, x )}')
    print(f'f({x}) =  {f(x)}')

    # graphic_Ln_x(val_table, x)

    S = splain(val_table)

    graphic_splain(val_table, S, x)


    return 0

if __name__ == "__main__":
    main()