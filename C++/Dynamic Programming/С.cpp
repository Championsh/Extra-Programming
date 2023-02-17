#include <iostream>

using namespace std;

int main(){

    int n, k, x, sum,a;

    cin >> n >> k;

    cin >> x;

    int K[n];
    int N[x];

    for (int i=0; i<x; i++){
        cin >> N[i];
        if (N[i]<3)
            K[N[i]]=0;
    }
    K[0]=1;
    K[1]=1;
    K[2]=2;
    sum=3;

    for (int i=3;i<n;i++){
        a=0;

        for (int j=0; j<x; j++){
            if (i==N[j])
                a++;
        }

        if (a==0){
            if (i<=k){
                K[i]=sum+1;
                sum+=K[i];
                cout << "1 stage:  " << K[i] << ' ' << sum << endl;
            }

            else{
                K[i]=sum+1-K[i-k-1];
                sum+=K[i]-K[i-k-1];
                cout << "2 stage:  " << K[i] <<  ' ' << sum << endl;
            }
        }
    }

    if(k==1)
        cout<<1;

    else
        cout<<K[n-1];

    return 0;

    }
