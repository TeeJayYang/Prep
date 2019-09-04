#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> elem_count;
        vector<int> res;

        if (nums1.empty() || nums2.empty()) return res;

        for (int i: nums1) {
            elem_count[i] = elem_count.find(i) != elem_count.end() ? elem_count[i] + 1 : 1;
        }

        for (int i: nums2) {
            if (elem_count.find(i) != elem_count.end() && elem_count[i] > 0){
                res.push_back(i);
                elem_count[i]--;
            }
        }
        return res;
    }
};
