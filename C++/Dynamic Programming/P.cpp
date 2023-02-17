#include <iostream>

using namespace std;

int main(){

    int n;

    cin >> n;
    n++;

    int K[n];
    int P[n];
    int N[n];
    int O[n];

    for (int i=0; i<n; i++)
        O[i]=100000;

    K[0]=0;
    P[0]=0;

    for (int i=0; i<n; i++){
        if (i<5){
            if (i!=0){
            K[i]=1+K[i-1];
            N[i]=i;
            P[i]=1;
            }
            else{
                K[i]=0;
                N[i]=0;
                P[i]=0;
            }
        }
        else{
        if (i==5){
            if (K[i-1]<K[i-5]){
                K[i]=1+K[i-1];
                N[i]=1;
                P[i]=1;
            }
            else{
                K[i]=1+K[i-5];
                N[i]=5;
                P[i]=5;
            }
        }
        else{
        if (i>=6){
            N[i] = i;

            if (i==6){
                K[i]=1+K[i-6];
                P[i]=6;
            }

            else{
                if (K[i-1]<K[i-5]){
                    if (K[i-1]<K[i-6]){
                        K[i]=1+K[i-1];
                        P[i]=1;
                    }
                    if (K[i-6]<=K[i-1]){
                        K[i]=1+K[i-6];
                        P[i]=1;
                    }
                }
                else{
                    if (K[i-5]<K[i-6]){
                        K[i]=1+K[i-5];
                        P[i]=5;
                    }
                    if (K[i-6]<=K[i-5]){
                        K[i]=1+K[i-6];
                        P[i]=6;
                        }
                    }
                }
            }
        }
        }
    }

    n--;

    cout << K[n] << endl;

    int i=0;
    int f=n;
    int k=n;
    while (f!=0){
        f=f-P[k];
        O[i]=P[k];
        i++;
        k=k-P[k];
    }

    while (i>0){
        cout << O[i-1] << ' ';
        i--;
    }
    cout << endl;
return 0;
}
