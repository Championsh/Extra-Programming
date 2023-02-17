#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
ifstream Fin;
ofstream Fout;
Fin.open("input.txt");
Fout.open("output.txt");
string x, x1, slov;
int p, m,k,i;
m = -10;
k = 0;
i = 0;
while (!Fin.eof())
{
if (getline(Fin, x))
{
x = x + ' ';
for (int i=0;i < x.size();i++) {
if (x[i] != ' ') {
k = k + 1;
slov = slov + x[i];
}
else {
if (k > m) {
m = k;
x1 = slov;
}
k = 0;
slov.clear();
}
}


}
}



Fout << x1;


Fin.close();
Fout.close();

return 0;
}
