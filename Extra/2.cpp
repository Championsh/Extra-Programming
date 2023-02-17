#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>

using namespace std;

main(){

int n,iss;
string s;
cin >> n;
int m [n] [n];
for (int i=0; i<n; i++){
    for (int j=0; j<n; j++){
        m [i] [j]=0;
        }
    }
for (int i=-1; i<n; i++)
{
    getline(cin, s);
    istringstream iss(s);
    int x;
    while (iss >> x) {
        if (x!=0)
            m [i] [x-1]=1;
        }
}
for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++)
        std::cout << " " << m[i][j];
        std::cout << std::endl;
    }
}
