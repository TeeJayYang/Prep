// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 0, hi = n;
        while (low < hi) {
            int mid = low + (hi - low)/2;
            bool isBad = isBadVersion(mid);
            if (isBad) hi = mid;
            else low = mid + 1;
        }
        return hi;
    }
};
