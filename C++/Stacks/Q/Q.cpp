#include <iomanip>
#include <string>
#include <queue>
#include <fstream>
using namespace std;

typedef struct {
  int x, y;
  } TPoint;
TPoint Point ( int x, int y )
{
  TPoint P;
  P.x = x; P.y = y;
  return P;
}

int main() {
typedef struct {
  int x, y;
  } TPoint;
const int XMAX = 5, YMAX = 5,
          NEW_COLOR = 2;
int A[YMAX][XMAX];
queue <TPoint> Q;
int i, j, x0, y0, color;
int k=0;
TPoint pt;
TPoint Point ( int x, int y )
while ( ! Q.empty() ) {
  pt = Q.front(); Q.pop();
  if ( A[pt.y][pt.x] == color ) {
    A[pt.y][pt.x] = NEW_COLOR;
    k++
    if ( pt.x > 0 )
        Q.push ( Point(pt.x-1,pt.y) );
    if ( pt.y > 0 )
        Q.push ( Point(pt.x,pt.y-1) );
    if ( pt.x < XMAX-1 )
        Q.push( Point(pt.x+1,pt.y) );
    if ( pt.y < YMAX-1 )
        Q.push( Point(pt.x,pt.y+1) );
    }
  }
Fout<< k;
Fout<< Q;
Fin.close();
Fout.close();
return 0;
}
