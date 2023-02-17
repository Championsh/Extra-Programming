#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main() {
    int n,i;
    cin >> n;
    int F[n+1];
    F[1]=1;
    F[2]=1;

    for (int i=3; i<n+1; i++){
        F[i]=F[i-1]+F[i-2];
    }

    cout << F[n];

}
