#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main() {

int k, n, minDist, minj;

cin >> n;

int m[n][n];
int col[n];
int ostov[n];
int P[n];

for (int i=0; i<n; i++){
        ostov [i]=10000;
        col[i]=1;
}

ostov[0]=0;

for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
        cin >> m [i] [j];
    }
}

cout << endl;
for ( int i = 0; i < n; i++ ) {
    for ( int j=0; j<n; j++ )
        cout << m[i][j] << ' ';
    cout << endl;
}

    minDist=100000;
    minj=-1;
    for (int j=0; j<n; j++)
        if ((col[j]==1)&&(ostov[j]<minDist)){
            minDist=ostov[j];
            minj=j;
        }
        if (minj!=-1){
            for ( int j=0; j<n; j++ ){
                if ((ostov[j]>ostov[minj] + m[minj][j])&&(m[minDist][j]>0)){
                    ostov[j]=ostov[minj] + m[minDist][j];
                    P[j]=minj;
                    }
            }
        col[minj]=0;
        }

cout <<endl;
for (int i=0; i<n; i++)
    cout << i+1 << " = "<< ostov[i]<<' ';

return 0;
}

5
0 7 10 6 0
7 0 2 0 18
10 2 0 1 13
6 0 1 0 20
0 18 13 20 0
