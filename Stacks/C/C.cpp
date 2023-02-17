#include <iomanip>
#include <string>
#include <stack>
#include <fstream>
#include <iostream>
using namespace std;
int main() {
ifstream Fin;
ofstream Fout;
const string L = "<([{", R = ">)]}";
string str;
stack <char> S;
bool err;
int i, p;
char c;
cin>> str;
err=false;
for ( i = 0; i < str.size(); i++ ) {
  p = L.find ( str[i] );
  if ( p >= 0 )
    S.push ( str[i] );
  p = R.find ( str[i] );
  if ( p >= 0 ) {
    if ( S.empty () )
      err = true;
    else {
      c = S.top(); S.pop();
      if ( p!= L.find(c) )
        err = true;
      }
    if ( err ) break;
    }
}
if ((!err )&(S.empty()))
    cout << "YES";
else
  cout << "NO";
return 0;
}
