// PracticesCpp.cpp : Defines the entry point for the console application.
//

#include <string>

using namespace std;


int main() {
  string s = "ghyuoko_";
  if (s.find("_") != string::npos) {
    size_t i = s.find("_");
    string s1 = s.substr(0, i);
    string s2 = s.substr(i + 1, s.size() - i - 1);
    string s_new = s2 + "_" + s1;
  }
  string t = "";
  bool b = t.empty();
  return 0;
}

