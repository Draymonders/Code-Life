# Cpp Primer 第5版 读书笔记

## 第1章 开始
- `Windows`系统中，输入文件结束符的方法是`Ctrl+Z`,在`UNIX`，是`Ctrl+D`

## 第2章 变量和基本类型
### 类型转换
```cpp
bool f = 42;
int c = f; // 结果 c = 1
```

### 作用域
```cpp
int reused = 42; // 全局变量
int main() {
    int reused = 0; // 局部变量
    cout << reused <<" " << unique<<endl; // 输出0 0 
    cout << ::reused << " " << unique <<endl; // 输出 42 0
    return 0;
}
```
注意 `::reused`的用法

### 指针
把int变量直接赋给指针是错误的操作。
```
int zero = 0;
int *p = zero; // error: invalid conversion from 'int' to 'int*' [-fpermissive]|
```
#### 指针和引用的区别
一旦定义了引用，就无法令其再绑定到另外的对象。
[C++中指针和引用的区别](https://www.cnblogs.com/dolphin0520/archive/2011/04/03/2004869.html)