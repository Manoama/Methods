from math import sqrt, copysign
import numpy as np
# Jacobi iterative method
# Var 6

# А = 
#     7       0.88        0,93        1.21
#     0.88    4.16        1,3         0.15
#     0.93    1.3         6.44        2
#     1.21    0.15        2           9

def Transpose(A):
    R = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    for i in range(len(A)):
        for j in range(len(A)):
            R[i][j] = A[j][i]

    return R



def print_Matrix(R):
    for r in range(len(R)):
        print(R[r])



def Mult_Matrix(A,B,C):
    Q = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    R = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(B)):
                Q[i][j] += A[i][k] * B[k][j]
    
    for i in range(len(Q)):
        for j in range(len(C)):
            for k in range(len(C)):
                R[i][j] += Q[i][k] * C[k][j]

    return R



def S_A(A):
    s = 0
    for i in range(len(A)):
        for j in range(len(A)):
            s += pow(A[i][j],2)
    return s



def S_d(A):
    s = 0
    for i in range(len(A)):
        s += pow(A[i][i],2)
    return s



def S_nd(A):
    s = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                s += pow(A[i][j],2)
    return s



# function that returns position of max non-diag elem of A
def max_nd_el_coord(A):
    point = list()
    max_elem = A[0][1]
    point = [0, 1]
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if max_elem < A[i][j]:
                max_elem = A[i][j]
                point = [i, j]
    return point 

def max_nd_el(A):
    max_elem = A[0][1]
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if max_elem < A[i][j]:
                max_elem = A[i][j]
    return max_elem


def find_cs(A, max_ij):
    i = max_ij[0]
    j = max_ij[1]
    mu = (2 * A[i][j]) / (A[i][i] - A[j][j])
    c = sqrt(0.5 * (1 + (1 / ( sqrt(1 + pow(mu,2) )))))
    s = copysign(1, mu) * sqrt(0.5 * (1 - (1 / ( sqrt(1 + pow(mu,2) )))))

    return [c,s]



def Jacobi_method(A, e):
    print("Program starts...\n\n-----------------------------------\n")
    print('A = \n')
    print_Matrix(A)
    print('------------------------------\n')

    l = 1
    while l < 20:
        k = 0
        max_elem = max_nd_el_coord(A)
        i = max_elem[0]
        j = max_elem[1]
        cs = find_cs(A, max_elem)
        c = cs[0]
        s = cs[1]
        T = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

        for k in range(4):
            if k != i and k != j:
                T[k][k] = 1
        
        T[i][i] = c
        T[j][j] = c
        T[i][j] = s
        T[j][i] = -s
        T_Tr = Transpose(T)

        # output T_ij and T`_ij
        print(f'----------------------------\nT_ij_{l} = \n')
        print_Matrix(T)
        print('------------------------------\n')

        print(f'----------------------------\nT`_ij_{l} = \n')
        print_Matrix(T_Tr)
        print('------------------------------\n')


        A = Mult_Matrix(T_Tr, A, T)

        # output A
        # print(f'----------------------------\nA_{l} = \n')
        # print_Matrix(A)
        # print('------------------------------\n')
        
        print(f'S_A_{l} = {S_A(A)}')
        print(f'S_d_{l} = {S_d(A)}')
        print(f'S_nd_{l} = {S_nd(A)}')

        l += 1   



        #  check
        max_el = max_nd_el(A)
        if abs(max_el) <= e:
            return (A[0][0], A[1][1], A[2][2], A[3][3])
            exit(1)
    return (A[0][0], A[1][1], A[2][2], A[3][3])
        





def main():

    A = [
        [7, 0.88, 0.93, 1.21],
        [0.88, 4.16, 1.3, 0.15],
        [0.93, 1.3, 6.44, 2],
        [1.21, 0.15, 2, 9]
    ]

    V = Jacobi_method(A, 0.001)
    print('\n---------------------\nVector = \n')    
    for x in V:
        print(f'\t[{x}]')


if __name__ == "__main__":
    main()