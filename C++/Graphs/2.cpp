#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>

using namespace std;

int main() {

int k, n, a, b, minDist, minj;

cin >> n;

int m[n][n];
int col[n];
int ostov[n];
int P[n];

for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
        cin >> m [i] [j];
        if (m[i][j]==0)
            m[i][j]=100000;
    }
}

cin >> b;
a=b-1;

for (int i=0; i<n; i++){
        ostov [i]=m[a][i];
        col[i]=1;
        P[i]=a;
}

ostov[a]=0;
P[a]=-1;
col[a]=0;

cout << endl;
for ( int i = 0; i < n; i++ ) {
    for ( int j=0; j<n; j++ )
        cout << m[i][j] << ' ';
    cout << endl;
}

for (int i=0; i<n-1; i++){
    minDist=100000;
    for (int j=0; j<n; j++)
        if ((col[j]==1)&&(ostov[j]<minDist)){
            minDist=ostov[j];
            minj=j;
        }
        col[minj]=0;
        for ( int j=0; j<n; j++ ){
            if (ostov[j]>ostov[minj] + m[minj][j]){
                ostov[j]=ostov[minj] + m[minj][j];
                P[j]=minj;
                }
        }
}

vector <int> mas;
    int i = n-1;
    while ( i != -1 )
      {
      mas.insert(mas.begin(), i);
      if (i == a) break;
      i = P[i];
      }
 cout << ostov[n-1] << endl;
    for (int i = 0; i < mas.size(); i++){
        cout << mas[i] + 1<< ' ';
    }

return 0;
}
