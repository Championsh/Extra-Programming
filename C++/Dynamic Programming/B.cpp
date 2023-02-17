#include <iostream>

using namespace std;

int main(){
int n;

cin>>n;
n++;

int K[n];
K[0]=0;
K[1]=1;
K[2]=1;
K[3]=2;

for (int i=4; i<n; i++){
    K[i]=K[i-1]+K[i-2];
}

cout << K[n-1];

return 0;
}
