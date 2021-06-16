#include <iostream>

using namespace std;

class HashTable{
    public:

}

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

        ArrayList(char type){
            switch (type){
                case 's':
                    string arr[1] = {};
                    break;
                case 'i':
                    int arr[1] = {}; 
                    break;
                case 'c':
                    char arr[1] = {};
                    break;    
            }

        }

};

class StringBuilder{
    public:
        void to_string(){
            string string;
            // Loop through array, concatenate letters. I think O(N) time, N = string length, since we have to loop through entire string. I don't know if this counts as copying string, cuz our runtime would be a lot more.
            for(int i=0; i<sizeof(arr); i++){
                string += arr[i];
            }
        }
    private: // use setters/getters? nahh
        ArrayList arr = {};
}
int main(){
    char arr[2] = {1, 2};
    cout << sizeof(arr) << endl;
    // Pointers are so weird
    cout << *(&arr + 1) - arr << endl;
    return 0;
}