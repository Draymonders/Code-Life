
## 输出字符串
有三种方式
```bash
#!/bin/bash

a="233
244"

echo $a
echo ${a}
echo "${a}"
```
### 输出结果
```
233 244
233 244
233
244
```
只有 `echo "${a}"`能输出换行符

> 所以推荐使用 echo "${variable}"
