# kmp

next数组表示 **前缀与后缀的最长匹配长度-1**

具体有什么意义呢？

接下来会来解释

比如 s串`abcabcabd`

```
a  b  c  a  b  c  a  b  d
-1 -1 -1 0  1  2  3  4 -1
```
你会发现 `如果next[i]不等于-1, s[i] == s[next[i]]`

这样做的意义是什么呢，是为了**快速回退**(减少不必要的字符匹配)


## 举例
```
s串
ississip
t串
issip
```
先分析出`t串`的`next`数组
```
i  s  s  i  p
-1 -1 -1 0  -1
```

然后去匹配,会发现如下情况不匹配了
```
i s s i s s i p 
i s s i p
```

由于我前一位`i`的`next[i]`为`0`，那么接下来将做如下匹配, 注意由上面的code到下面的code仅仅需要一步
```
i s s i s s i p
      i s s i p
```


## code
```c++
class Solution {
public:
    int strStr(string s, string t) {
        if (t == "") return 0;
        int l1 = s.size(), l2 = t.size();

        int next[l2] = {0};
        next[0] = -1;
        for (int i=1; i<l2; i++) {
            int k = next[i-1];
            while (k != -1 && t[k+1] != t[i])  k = next[k];
            if (t[i] == t[k+1]) {
                next[i] = k+1;
            } else {
                next[i] = -1;
            }
        }
        
        int i = 0, j = 0;
        while (i < l1) {
            if (s[i] == t[j]) {
                i++,j++;
                if (j == l2) {
                    return i - l2;
                }
            } else {
                if (j == 0) {
                    i++;
                } else {
                    j = next[j-1] + 1;
                }
            }
        }
        return -1;
    }
};
```