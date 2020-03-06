# 收录一些会用到的一些cpp的feature

## std::initializer_list
Before
```c++
vector<int> v;  // python: v = [1,2,3,4]
v.push_back(1);
v.push_back(2);
v.push_back(3);
v.push_back(4);
```

After:
```c++
vector<int> v{1, 2, 3, 4};
initializer_list<int> l = {1, 2, 3, 5};
vector<int> v(l); // copy l into v
```

## auto
Before
```c++
set<int> st;
typedef set<int>::iterator IT;
typedef set<int>::const_iteratore CIT;

for (IT it=st.begin(); it != s.end(); ++it)

// const begin const end
for (CIT cit=st.cbegin(); it != s.cend(); ++it)
```

After
```c++
for (auto it =st.begin(); it != s.end(); ++it)

for (auto cit=st.cbegin(); it != s.cend(); ++it)

auto it = st.find(x);
```


## Structured binding (Since C++17)
Before
```c++
pair<int, float> p(1, 3.14);
int x = p.first;
float y = p.second;

python:
p = (1, 3.14)
x, y = p
```

After
```c++
const auto& [x, y] = p
```


Before
```c++
set<int> s;
auto kv = s.insert(x); //返回的是一个pair， 第一个是迭代器， 第二个是插入成功与否
auto it = kv.first;
bool success = kv.second;
```

After
```c++
set<int> s;
const auto [it, success] = s.insert(x);
```


## range based for loop

Before
```c++
set<int> s{1, 2, 3, 4, 5};
for (auto it =s.begin(); it != s.end(); ++it)
```

After
```c++
for (int x : s)
```

### map遍历
```c++
map<string, int> mp;
for (auto&& kv: mp) {
    cout << kv.first <<" " << kv.second <<endl;
}


for (auto&& [k, v] : mp) {
    cout << k << " " << v <<endl;
}
```

## lambda
Before
```c++
bool cmp(const pair<int, int>& a, 
    const pair<int, int>& b) {
    return a.second < b.second;
}

int main() {
    vector<pair<int,int>> v = ...;
    sort(begin(v), end(v), cmp);
}
```

After
```c++
sort(begin(v), end(v), [](const auto& a, 
    const auto & b) {
    return a.second < b.second;
});
```

### 回调函数
```c++
class Foo {
public:
    void Init() {
        // 捕获指针
        bar->onUpdate([this](const auto& data) {
            this->onUpdate(data);
        })
    }
private:
    Bar* bar;
    void onUpdate(const vector<int>& data) { ... }
};
```