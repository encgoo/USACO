//
//  main.cpp
//  Farm_address
//
//  Created by Yongjian Feng on 2/15/20.
//  Copyright © 2020 Yongjian Feng. All rights reserved.
//

#include <iostream>
#include <string>
#include "stdio.h"

using namespace std;

size_t find_min_unique(const string& in_str){
    size_t min_unique = in_str.size();
    // len of string is always unique try one less
    size_t sz_test = min_unique - 1;
    while (sz_test > 0){
        int i = 0;
        bool found_multiple = false;
        for (i = 0; i < in_str.size() - sz_test; ++i){
            string sub = in_str.substr(i, sz_test);
            size_t pos = in_str.find(sub, i + 1);
            if (pos != string::npos){
                // found multiple
                found_multiple = true;
                break;
            }
        }
        if (found_multiple){
            break;
        }
        // if everything is still fine, update min_unique
        min_unique = sz_test;
        // decrement sz_test
        sz_test--;
    }
    
    return min_unique;
}
int main(int argc, const char * argv[]) {
    string str("ABCDABC");
    
    size_t min_unique = find_min_unique(str);
    printf("Min unique is %d\n", min_unique);
    
    return 0;
}
