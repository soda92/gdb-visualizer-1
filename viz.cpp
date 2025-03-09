#include <string>
#include <vector>
using namespace std;

namespace MyNamespace {
class MyClass {
public:
  int member1;
  int member2;
};
} // namespace MyNamespace

class Rectangle {
private:
  int height;
  int width;

public:
  Rectangle() : height(3), width(5) {}
  Rectangle(int H) : height(H), width(H * 2 - 1) {}
  Rectangle(int H, int W) : height(H), width(W) {}
  int GetHeight() { return height; }
  int GetWidth() { return width; }
};

int main() {
  MyNamespace::MyClass a;
  a.member1 = 4;
  a.member2 = 2;

  Rectangle r;
  vector<string> vs = {"hello0", "aaa"};
  return 0;
}