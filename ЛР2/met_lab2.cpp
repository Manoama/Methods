#include<iostream>
#include<cmath>
using namespace std;

void print_vector(double T[4],string name)
{
    cout << name << ":" << endl;
    for (int i = 0; i < 4; i++)
        cout << "\t[" << T[i] << "]" << endl;
}


void print_Matrix(double T[4][4], string name)
{
    cout << "Matrix "<< name << ":" << endl;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
            cout << T[i][j] << " ";
        cout << endl;
    }
}

int main()
{
    double A[4][4] = {
        {5.5, 7, 6, 5.5},
        {7, 10.5, 8, 7},
        {6, 8, 10.5, 9},
        {5.5, 7, 9, 10.5}
    };

    double B[4] = {23, 32, 33, 31};

    double L[4][4] = {
        {0, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 0}
    };
    cout << endl;
    print_Matrix(A,"A");
    cout << endl;
    print_vector(B,"B");
    cout << endl;
    print_Matrix(L,"L");
    cout << endl;

// 1. Create L-matrix:
    // 1.1 L[0][0]:
    L[0][0] = sqrt(A[0][0]);
    print_Matrix(L,"L");
    cout << endl;
    //1.2 L[j][0]:
    for (int i = 1; i < 4; i++)
    {
        L[i][0] = A[i][0] / L[0][0];
        print_Matrix(L,"L");
        cout << endl;
    }
    
    //1.3 L[i][i] and L[i][j] (j < i):
    for (int i = 1; i < 4; i++)
    {
        double sum_d = 0;
        double sum_nd = 0;

        for (int j = 1; j <= i; j++)
        {
            if (i == j)
            {
                sum_d = 0;
                for (int k = 0; k < j; k++)
                    sum_d += pow(L[i][k], 2);
                
                
                L[i][i] = sqrt(A[i][i] - sum_d);
                print_Matrix(L,"L");
                cout << endl;
            }
            else
            {
                sum_nd = 0;
                for (int k = 0; k < j; k++)
                    sum_nd += L[i][k] * L[j][k];
                
                L[i][j] = (A[i][j] - sum_nd) / L[j][j];
                print_Matrix(L,"L");
                cout << endl;
            }
        }
        
    }
    
    print_Matrix(L,"L");

// 2. Reverse:
    // 2.1. Y:
    double Y[4] = { 0 };
    Y[0] = B[0] / L[0][0];
    for (int i = 1; i < 4; i++)
    {
        double sum = 0;
        for (int k = 0; k < i; k++)
            sum += L[i][k] * Y[k];
        
        Y[i] = (B[i] - sum) / L[i][i];
    }

    print_vector(Y,"Y");
    
    //2.2 X:
    double X[4] = { 0 };
    X[3] = Y[3] / L[3][3];
    for (int i = 2; i >= 0; i--)
    {
        double sum = 0;
        for (int k = i + 1; k < 4; k++)
            sum += L[k][i] * X[k];
        
        X[i] = (Y[i] - sum) / L[i][i];
    }
    cout << endl;
    print_vector(X,"X");

// 3. Check correctness
    double R[4] = { 0 };
    for (int i = 0; i < 4; i++)
    {
        double sum = 0;
        for (int j = 0; j < 4; j++)
        {
            sum += A[i][j] * X[j];
        }
        R[i] = sum;
    }

    for (int i = 0; i < 4; i++)
        R[i] -= B[i];
    
    cout << endl;

    print_vector(R,"(Ax - b)");
    

    return 0;
}