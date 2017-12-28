// PracticesCpp.cpp : Defines the entry point for the console application.
//

#include <string>

using namespace std;


int main() {
  string s = "ghyuoko_";
  if (s.find("_") != string::npos) {
    size_t n = s.find("_");
    string s1 = s.substr(0, n);
    string s2 = s.substr(n + 1, s.size() - n - 1);
    string s_new = s2 + "_" + s1;
  }
  string t = "";
  bool b = t.empty();
  return 0;
}

