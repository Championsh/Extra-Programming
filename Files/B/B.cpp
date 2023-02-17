#include <fstream>
#include <iomanip>
using namespace std;
main(){
ifstream Fin;
ofstream Fout;
Fin.open("input.txt");
Fout.open("output.txt");
int z;
double mi, ma, x,k;
mi=100000000;
ma= -1;
k=0;
while( ! Fin.eof() )
  {
  if ( Fin >> x )
  {
      z=x;
      if ((z>0)&(z%2==0)){
            k++;
      if (z>ma){
        ma=z;
      }
      if (z<mi){
        mi=z;
      }
      }
   }
  }
if (k>0){
Fout << mi << ' ' << ma;
}
else{
    Fout << '0';
}
Fin.close();
Fout.close();
return 0;
}
