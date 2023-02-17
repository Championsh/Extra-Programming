#include <iomanip>
#include <string>
#include <stack>
#include<fstream>
using namespace std;
int main() {
ifstream Fin;
ofstream Fout;
stack <string> S;
string x,k;
int ce;
ce = 0;
k.clear();
Fin.open("input.txt");
Fout.open("output.txt");
while (!Fin.eof())
    {
        if (getline(Fin, x))
            {
                if (x[0]=='+') {
                    S.push(x.substr(1,x.size()));
                    }
                else {
                    if (!S.empty()) {
                        S.pop();
                        }
                    else {
                        Fout<<"ERROR";
                        ce = 1;
                        break;
                    }
                }
        }
}
if ((S.empty() == true)&(ce!=1)) {
    Fout<<"EMPTY";
}
else {
    while ((!S.empty())&(ce!=1)) {
        k = S.top()+' '+k;
        S.pop();
    }
}
Fout<<k;
Fin.close();
Fout.close();
return 0;
}
