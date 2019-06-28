## chvt 切换终端
用法
1是终端
7是图形界面
```
sudo chvt 1 or 7
```

## cp 复制文件/目录
```
-a : 通常在复制目录时使用，保存链接，文件属性并递归复制目录
-f：若文件在目标路径中则强制覆盖
-i：交互式
-r：递归复制整个目录
-p：除了复制内容 还把修改时间和访问权限也复制到新文件中
```

## 文件链接命令

```
ln [参数] 目标 链接名

软链接（符号链接） ln -s   source  target 
硬链接 （实体链接）ln       source  target
```
### 软硬链接区别
区别：
1. 硬链接原文件/链接文件公用一个inode号，说明他们是同一个文件，而软链接原文件/链接文件拥有不同的inode号，表明他们是两个不同的文件；
2. 在文件属性上软链接明确写出了是链接文件，而硬链接没有写出来，因为在本质上硬链接文件和原文件是完全平等关系；
3. 链接数目是不一样的，软链接的链接数目不会增加；
4. 文件大小是不一样的，硬链接文件显示的大小是跟原文件是一样的。而这里软链接显示的大小与原文件就不同了，BBB大小是95B，而BBBsoft是3B。因为BBB共有3个字符
5. 软链接没有任何文件系统的限制，任何用户可以创建指向目录的符号链接

### 参考文章
[linux硬链接与软链接](https://www.cnblogs.com/crazylqy/p/5821105.html)

## 显示文本文件内容
### cat 命令
```
cat [选项] file

-n: 显示行号
-b 显示行号，对空白行不编号
-v: 用一种特殊形式显示控制字符
```
### more 命令
```
more [选项] file

-num 一次显示的页数
按Space下一页，Q退出
```
### less命令
```
less [选项] file

使用Page Up PageDown 控制翻页 Q退出
```
### head 命令
```
head [选项] file

只显示文件的头几行内容
```

### tail 命令
```
tail [选项] file

// +num: 从第num行以后开始显示, 自己测试不能使用
-num: 从距文件尾num行处显示

只显示文件的末尾几行内容
```

## find 查找文件命令
```
find [路径] [参数] [文件名]

参数如下
-name: 文件名
-lname：指定文件的所有链接文件
-user：用户拥有的文件
-group：组拥有的文件
-a and 与
-o or 或者
! not 否定
```

## 文件内容查询命令
### grep命令
以指定的查找模式搜索文件
```
grep [选项] 文件名1, 文件名2，...，文件名n

选项有如下
-i : 忽略字母大小写
-l：仅输出包含目标串的文件名
-v： 输出不包含目标字符串的行
-n: 输出每个含有目标字符串的行以及行号
```
### egrep命令
检索扩展的正则表达式

### fgrep命令
检索固定字符串，并不识别正则表达式

## 文件处理命令
### sort命令
逐行对文件中的内容进行排序
```
sort [选项] file

-d 使sort忽略标点符号和一些其他特殊字符，按照字典序排序
-f: 不区分大小写进行排序
-n： 按照数值排序
-r：反向排序
-o arg: 输出置于arg中
```
### wc 文件统计命令
```
wc [选项] file
-c: 统计字符数
-w: 统计单词数
-l：统计行数
```

## Vim

```
vi -r file # 在上次使用vi编辑时发生崩溃，恢复file
```

### 在编辑多个文件时候
```
:n 下一个文件
:e# 回到刚才编辑的文件
```

### 撤销操作
```
撤销前一个命令 输入"u"
撤销对一行的修改  输入"U"
```

### 删除文本
```
删除一个字符 "x"
删除一词  "dw"
删除一行 "dd"
```

### 复制和粘贴
```
复制一行内容 "yy"
粘贴 "p"
剪切 "dd"
```

### 查找字符串
```
输入查找内容  "/"
跳到下一个出现处 "n"
跳到上一个出现处 "N"
```

### 复制文本块
```
:1,4 copy 7 #第1-4行的文本复制到第7行之后
```

### 移动文本块
```
:1,8 move 7 #第1-8行的内容移动到7行后
```

### 另存文本块
```
:1,8 write file2 #把1到8行的内容重保存file2
```
### 追加文本块
```
:90,100 w>>file2 #把90到100行的内容追加到file2
```
### 保存并退出
智障自动退出hhh
```
命令模式下 "ZZ"
```