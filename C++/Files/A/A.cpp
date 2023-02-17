#include <fstream>
#include <iomanip>
using namespace std;
main(){
ifstream Fin;
ofstream Fout;
Fin.open("input.txt");
Fout.open("output.txt");
double S, x, k;
S = 0;
k = 0;
while( ! Fin.eof() )
  {
  if ( Fin >> x )
  {
   S = S + x;
   k++;
   }
  }
Fout << fixed << setprecision(3) << S/k;
Fin.close();
Fout.close();
return 0;
}
