Task 4:
#include <iostream>
using namespace std;

double quest2(int n) {
    if (n == 0) return 0;
    return 1.0 / n + quest2(n - 1);
}

int main() {
    int n;
    cout << "enter value: ";
    cin >> n;

    double result = quest2(n);
    cout << "Sum: " << result << endl;

    return 0;
}


Task 5:

 #include <iostream>
using namespace std;

double quest5(int n) {
    if (n == 0) return 0;
    return 1.0 / n + quest5(n - 1);
}
double quest5() {
    int n;
    cout << "enter a value (without parameter): ";
    cin >> n;
    return quest5(n);
}

int main() {
    double result = quest5();  
    cout << "overload: " << result << endl;
    return 0;
}
