class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0, end = s.size() - 1;
        while (start < end) {
            if (!isalnum(s[start])) start++;
            else if (!isalnum(s[end])) end--;
            else if (tolower(s[start++]) != tolower(s[end--])) return false;
        }
        return true;
    }
    bool isPalindrome2(string s) {
        transform(s.begin(), s.end(), s.begin(), [](char c){ return tolower(c); });
        s.erase(remove_if(s.begin(), s.end(), [](char c) { return !isalnum(c); }), s.end());
        string rev = s;
        reverse(rev.begin(), rev.end());
        return rev == s;
    }
};
