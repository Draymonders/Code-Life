## Redis中的字典
有两个重要的字段`ht`数组(hashtable), 另外一个`rehashidx`

`rehashidx`记录了目前rehash的进度，如果没有进行rehash，值为-1

`链地址法`解决冲突

## rehash

![rehash步骤](./dict.png)

## 渐进式rehash
![渐进式rehash步骤](./dict2.png)
