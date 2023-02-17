#include <fstream>
#include <iomanip>
#include <string>
using namespace std;
main(){
ifstream Fin;
ofstream Fout;
Fin.open("input.txt");
Fout.open("output.txt");
int z;
double ma,k;
string mac,x;
ma=-1;
while( !Fin.eof() )
  {
  if (getline(Fin, x))
  {
      z=x.length();
      if (z>0){
      if (z>ma){
        mañ=x;
      }
      }
   }
  }
Fout << mac;
Fin.close();
Fout.close();
return 0;
}
