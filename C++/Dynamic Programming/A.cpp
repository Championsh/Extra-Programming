#include <iostream>

using namespace std;

int main(){
int n;

cin>>n;

int m=2;
int F[2];
F[0]=1;
F[1]=1;
int x=0;
while (F[1]<n){
    m++;
    x=F[1];
    F[1]=F[0]+F[1];
    F[0]=x;
    }

if (F[1]==n)
    cout<<m;

else
    cout<<"-1";

return 0;
}
