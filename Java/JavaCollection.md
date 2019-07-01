## Java集合
### ArrayList
数组的默认大小为 10。
```java
private static final int DEFAULT_CAPACITY = 10;
```
添加元素时使用 ensureCapacityInternal() 方法来保证容量足够，如果不够时，需要使用 grow() 方法进行扩容，新容量的大小为 `oldCapacity + (oldCapacity >> 1)`，也就是旧容量的 1.5 倍。

### Vector
数组的默认大小为 10。

Vector 每次扩容请求其大小的 2 倍空间，而 ArrayList 是 1.5 倍。


Vector 是同步的，因此开销就比 ArrayList 要大，访问速度更慢。最好使用 ArrayList 而不是 Vector，因为同步操作完全可以由程序员自己来控制；
可以使用collections的同步list的方法
```java
List<String> list = new ArrayList<>();
List<String> synList = Collections.synchronizedList(list);
```
### CopyOnWriteArrayList
```java
public boolean add(E e) {
    final ReentrantLock lock = this.lock;
    lock.lock();
    try {
        Object[] elements = getArray();
        int len = elements.length;
        Object[] newElements = Arrays.copyOf(elements, len + 1);
        newElements[len] = e;
        setArray(newElements);
        return true;
    } finally {
        lock.unlock();
    }
}

final void setArray(Object[] a) {
    array = a;
}
```

#### 适用场景
CopyOnWriteArrayList 在写操作的同时允许读操作，大大提高了读操作的性能，因此很适合读多写少的应用场景。

但是 CopyOnWriteArrayList 有其缺陷：

- 内存占用：在写操作时需要复制一个新的数组，使得内存占用为原来的两倍左右；
- 数据不一致：读操作不能读取实时性的数据，因为部分写操作的数据还未同步到读数组中。
所以 CopyOnWriteArrayList 不适合内存敏感以及对实时性要求很高的场景。

## hashMap
### hash为2的幂的作用
1. `key & (hash - 1)`等同于`key % hash`，但前者效率比后者高
2. 扩容的时候，`table cap`变为`2 * table cap`,rehash仅仅需要判断`key & hash`如果为0，还是原来的`table[old]`,否则是`table[old+table cap]`
### mask码的作用
先考虑如何求一个数的掩码，对于 10010000，它的掩码为 11111111，可以使用以下方法得到：
```
mask |= mask >> 1    11011000
mask |= mask >> 2    11111110
mask |= mask >> 4    11111111
```
mask+1 是大于原始数字的最小的 2 的 n 次方。
```
num     10010000
mask+1 100000000
```
以下是 HashMap 中计算数组容量的代码：
```
static final int tableSizeFor(int cap) {
    int n = cap - 1;
    n |= n >>> 1;
    n |= n >>> 2;
    n |= n >>> 4;
    n |= n >>> 8;
    n |= n >>> 16;
    return (n < 0) ? 1 : (n >= MAXIMUM_CAPACITY) ? MAXIMUM_CAPACITY : n + 1;
}
```
