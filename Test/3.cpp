#include <iostream>

using namespace std;

int main(){
int n;
int f;

cin>>n;
cin>>f;
n++;

int K[n];
K[n-1]=1;

for (int i=n-2; i>f-1; i--){
    if (i*2<=(n-1))
        K[i]=K[i+1]+K[i*2];
    else
        K[i]=K[i+1];
}

cout << K[f];

return 0;
}
