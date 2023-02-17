#include <iostream>
#include <queue>

using namespace std;

int main()

{
int n;
cin >> n;
int m [n] [n];
for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
        cin >> m [i] [j];
    }
}
for (int i=0; i<n;i++){
    int k=0;
    for (int j=0;j<n;j++){
        if (m[i][j] !=0){
            k++;
            cout << j+1 << ' ';
    }
    }
    if (k==0)
        cout << '0';
    cout << ' ' << endl;
}
}
