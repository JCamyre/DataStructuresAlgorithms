#include <iostream>;

using namespace std;

// class HashTable{
//     public:

// }

// Maybe have ArrayList be whatever datatype they want, add that to __init__(). Also need __init__ for initialiizng.
class ArrayList{
    public:
        void add(string val) {
            if(sizeof(arr) + 1 > arr.max){
                arr = arr[arr.max*2];
            }
            arr.append(val);
        }
    private:
        string arr[1] = {};

};

class StringBuilder{
    public:
        void to_string(){

        }
    private:
        ArrayList = {};
}
int main(){


    return 0;
}