#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main() {

int k,n,x;
k=0;
x=0;

cin >> n;

int m[n][n];

for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
        cin >> m [i] [j];
    }
}

for ( int i = 0; i < n; i++ ) {
  for (int j=0; j<n; j++){
        if (m[i][j]!=0){
        if ((m[i][j]==m[j][i])&&(m[i][j]!=0)){
            k+=1;
            m[i][j]=0;
            m[j][i]=0;
        }
        if (m[i][j]!=m[j][i]){
            if (m[j][i]==0)
                x+=1;
            if (m[j][i]!=0)
                x+=2;
            m[i][j]=0;
            m[j][i]=0;
        }
        }
  }
}
cout << x << ' ' << k;
return 0;
}
