## 一个我也不知道怎么用的语法

语法如下
> 需要注意的一点是  比较函数里面写的是 a < b, 实际返回结果`que.top()`是最大值 对立的..
```cpp
auto cmp = [](int a,int b) {
    return a < b;
};
priority<int, vector<int>, decltype(cmp)> que(cmp);
```