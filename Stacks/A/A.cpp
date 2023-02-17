#include <iomanip>
#include <string>
#include <stack>
#include<fstream>
using namespace std;
int main() {
ifstream Fin;
ofstream Fout;
stack <int> S;
int x;
Fin.open ( "input.txt" );
while ( Fin >> x )
  S.push ( x );
Fin.close();
Fout.open ( "output.txt" );
while ( ! S.empty() )
  {
  Fout << S.top() << ' ';
  S.pop();
  }
Fout.close();
return 0;
}
