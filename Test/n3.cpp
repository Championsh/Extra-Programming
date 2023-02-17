#include <iostream>
#include <math.h>

using namespace std;

int main(){
int n;

cin>>n;
n++;

int K[n];
K[0]=0;
K[1]=2;
K[2]=2;

for (int i=3; i<n; i++){
    if ((i/10!=2)&&(i/10!=2)&&(i/10!=2)&&(i/10!=2)){
        int f = int (sqrt(i));
        if (f*f==i)
            K[i]=K[i-1] + K[f];
        else
            K[i]=K[i-1];
    }
}

cout << K[n-1];

return 0;
}
