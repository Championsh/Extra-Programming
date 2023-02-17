#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main() {

int i, j, k, iMin, jMin, minDist, c, n;

cin >> n;

int m[n][n];
int col[n];
int ostov[n-1][2];
int l=0;

for (i = 0; i < n; i ++)
    col[i] = i;

for (int i=0; i<n-1; i++){
    for (int j=0; j<n-1; j++){
        ostov [i] [j] = -1;
    }
}

for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
        cin >> m [i] [j];
    }
}

for ( k = 0; k < n-1; k++ ) {
  int minDist = 100000;
  iMin=-1;
  jMin=-1;
  for ( i = 0; i < n; i ++ ){
    for ( j = 0; j < n; j ++ ){
      if (( col[i] != col[j]) && (m[i][j] <  minDist) && (m[i][j]!=0)) {
        iMin = i;
        jMin = j;
        minDist = m[i][j];
        }
      }
    }
    if (jMin!=-1){
        ostov[l][0] = iMin + 1;
        ostov[l][1] = jMin + 1;
        c = col[jMin];
        l++;
        for ( i = 0; i < n; i ++ )
            if ( col[i] == c )
                col[i] = col[iMin];
    }
}

for (i=0; i<n;i++){
    for (j=0; j<n-1;j++){
            if (ostov [j][0] > ostov [j+1][0]){
                swap(ostov[j][0],ostov[j+1][0]);
                swap(ostov[j][1],ostov[j+1][1]);
            }
        }
    }

for (i=0; i<n;i++){
    for (j=0; j<n-1;j++){
        if (  ( ostov [j][1] > ostov [j+1] [1] ) && ( ostov [j] [0] == ostov [j+1] [0] )  )
            swap(ostov[j][1],ostov[j+1][1]);
        }
    }

for ( i = 0; i < n; i ++ ){
    if ( (ostov [i] [0] > 0)  && (ostov [i] [1] > 0) )
        cout <<ostov[i][0]<< " " << ostov[i][1] << endl;
}
return 0;
}
