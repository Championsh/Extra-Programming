#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>

using namespace std;

main(){

ifstream Fin;
ofstream Fout;
Fin.open("input.txt");
Fout.open("output.txt");

int n,iss,k,f,j;
string s;
j=0;
while(getline(Fin, s))
{
    k=0;
    f=0;
    istringstream iss(s);
    string x;
    for (int i =0;i< s.size(); i++) {
        x=s[i];
        if (x=="A")
            k++;
        if (x=="E")
            f++;
    }
    if (k>f)
        j++;
}

Fout << j;

Fin.close();
Fout.close();

}
