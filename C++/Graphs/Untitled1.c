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
        ostov [i]=1000;
        col[i]=1;
}

a=0;
ostov[a]=0;

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

for (int i = 0; i < n-1; i++ ) {
      int minDist = 99999;
      for ( int j = 0; j < n; j ++ )
        if ( col[j]==1 && ostov[j] < minDist) {
          minDist = ostov[j];
          minj = j;
          }
      col[minj] = 0;
      for ( int j = 0; j < n; j ++ )
        if ( ostov[minj]+m[minj][j] < ostov[j] ) {
          ostov[j] = ostov[minj] + m[minj][j];
          P[j] = minj;
          }
    }

cout <<endl;
for (int i=0; i<n; i++)
    cout << i+1 << " = "<< ostov[i]<<' ';

return 0;
}
