## sorted set为什么使用skip list 和 dict
1. 使用`dict[key] = score`, 可以`O(1)获取对象的分值`
2. 使用`skip list`，可以`O(logn)`获取区间范围的元素

![sorted set为什么使用skip list 和 dict](./sortedset.png)