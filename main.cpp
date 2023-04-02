#include "bubblesort.h"
#include "heapsort.h"
#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <cmath>

using namespace std;
using namespace std::chrono;

int main() {
    // create a vector with random elements
    ofstream file("output.txt");

    if (file.is_open()) {
        file << "n_values, bubblesort(ms), heapsort(ms)" << endl;
        vector<int> arr,arr1;
        for (int i = 1; i <= 6; i++) {
            int n = pow(10, i);

            for (int j = 0; j < n; j++) {
                arr.push_back(rand());
            }

            arr1 = arr; //arr copy

            // measure the execution time of Bubble Sort
            auto start = high_resolution_clock::now();
            bubbleSort(arr);
            auto stop = high_resolution_clock::now();
            auto duration = duration_cast<milliseconds>(stop - start);

            // store value
            file << n << ", " << duration.count();
            
            //measure the execution time of Bubble Sort
            start = high_resolution_clock::now();
            heapSort(arr1);
            stop = high_resolution_clock::now();
            duration = duration_cast<milliseconds>(stop - start);
            
            // store value
            file << ", "<< duration.count() << endl;

        }

    }    else {
        cout << "Unable to open file" << endl;
    }
    file.close();



    return 0;
}
