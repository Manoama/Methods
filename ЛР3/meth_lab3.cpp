#include<iostream>
#include<string>
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
    //  double A[4][4] = {
    //     {5.5, 7, 6, 5.5},
    //     {7, 10.5, 8, 7},
    //     {6, 8, 10.5, 9},
    //     {5.5, 7, 9, 10.5}
    // };

    double A[4][4] = {
        {20, 2, 3, 7},
        {1, 12, -2, -5},
        {5, -3, 13, 0},
        {0, 0, -1, 15}
    };

    // double B[4] = {23, 32, 33, 31};
    double B[4] = {5, 4, -3, 7};    

    double e = 0.0001;

    //  Ax = B => x = Cx + d
    // Create matrix C
    double C[4][4] = { 0 };
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (i == j)
            {
                C[i][j] == 0;
            }
            C[i][j] = - (A[i][j] / A[i][i]);
        }        
    }
    // Create vector d
    double X[4] = {0};
    double X_prev[4] = {0};
    
    // X_0:
    for (int i = 0; i < 4; i++)
    {
        X_prev[i] = B[i] / A[i][i];
    }
    
    // condition
    bool cond = 1;
    int iter_count = 1; 
    while (cond)
    {
        for (int i = 0; i < 4; i++)
        {
            X[i] = B[i] / A[i][i];
            for(int j = 0; j < 4; j++)
            {
                if(i != j)
                    X[i] += C[i][j] * X_prev[j];
            }
        }
        cout << "Iteration " << iter_count <<":"<< endl;
        print_vector(X,"X");
        print_vector(X_prev,"X_prev");

        for (int i = 0; i < 4; i++)
        {
            if (abs(X[i] - X_prev[i]) > e)
            {   
                cout << "| X[" << i << "] - X_prev[" << i << "] | = " << abs(X[i] - X_prev[i]) << " > " << e << " = eps" << endl;
                cout << "So continue...\n---------------------------------------" << endl; 
                cond = true;    
                break;
            }
            else
            {
                cout << "| X[" << i << "] - X_prev[" << i << "] | = " << abs(X[i] - X_prev[i]) << " < " << e << " = eps" << endl; 
                cond = false;
            }
        }

        for (int i = 0; i < 4; i++)
        {
            X_prev[i] = X[i];
        }
        
        iter_count++;
    }
    
    
    

    

    
    return 0;
}