#include <iostream>

using namespace std;

int main(){
int n;

cin>>n;
n++;

int K[n];
K[0]=1;
K[1]=1;

for (int i=2; i<n; i++){
    if (i<8)
        K[i]=K[i-1];
    else{
        if (i<10)
            K[i]=K[i-1]+K[i-8];
        else
            K[i]=K[i-1]+K[i-8]+K[i-10];
    }
    cout << i << " - " << K[i] << endl;
}

cout << K[n-1];

return 0;
}
