#include <fstream>
#include <iomanip>
#include <string>
using namespace std;
int main(){
ifstream Fin;
ofstream Fout;
Fin.open("input.txt");
Fout.open("output.txt");
string x,b,v;
int p,z,k,i;
z=-1;
k=0;
i=0;
while (!Fin.eof()){
    if (getline(Fin, x)){
        x=x+' ';
        for (int i=0;i<x.size();i++){
            if (x[i]!= ' '){
                k++;
                v=v+x[i];
            }
            else{
                if (k>z){
                    z=k;
                    b=v;
                }
                k=0;
                v.clear();
            }
        }
}
}
Fout<<b;
Fin.close();
Fout.close();
return 0;
}
